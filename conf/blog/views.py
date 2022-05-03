from django.shortcuts import render
from django.views.generic import *
from .models import Blog
# Create your views here.

# blog list
class BlogList(ListView):
    template_name = 'templates/blog_list.html'
    def get_queryset(self):
        return Blog.objects.all()
    