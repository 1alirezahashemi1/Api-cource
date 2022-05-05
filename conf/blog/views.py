from django.shortcuts import render , get_object_or_404
from django.views.generic import *
from .models import Blog
# Create your views here.

# blog list
class BlogList(ListView):
    template_name = 'templates/blog_list.html'
    def get_queryset(self):
        return Blog.objects.all()
    
# Blog Detail

class BlogDetail(DetailView):
    def get_object(self):
        return get_object_or_404(Blog.objects.filter(status = True) , pk = self.kwargs.get("pk"))
        