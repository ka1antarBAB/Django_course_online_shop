from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages

from products.models import Product, Comment
from products.forms import CommentForm

# Create your views here.


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.active_products_manager.all()


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(active=True)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)

        obj.product = product
        return super().form_valid(form)
