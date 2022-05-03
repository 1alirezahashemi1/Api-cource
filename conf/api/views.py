from django.shortcuts import render
from rest_framework.generics import *
from .serializers import BlogSerializer
from blog.models import Blog
# Create your views here.

class Apilist(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer