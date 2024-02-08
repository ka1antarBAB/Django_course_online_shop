from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy

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
        product = self.get_object()
        active_comments = Comment.active_comment_manager.filter(product=product)
        context['active_comments'] = active_comments
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


# @login_required
# def book_detail_view(request, pk):
#     #book
#     book = get_object_or_404(Book, pk=pk)
#     comments = book.comments.all()
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.book = book #book
#             comment.user = request.user
#             comment.save()
#             comment_form = CommentForm()
#             redirect_url = reverse_lazy('books:book_detail')
#     if request.method == 'GET':
#         comment_form = CommentForm()
#     return render(request, 'books/book_detail.html', context={
#         'book': book,
#         'comments': comments,
#         'comment_form': comment_form
#     })
