from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogModel
# Create your views here.
class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel