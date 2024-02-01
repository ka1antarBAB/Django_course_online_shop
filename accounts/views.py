from django.shortcuts import render
from django.views import generic
from django.views.generic import edit
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')

