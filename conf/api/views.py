from django.shortcuts import render
from rest_framework.generics import *
from django.contrib.auth.models import User
from .serializers import BlogSerializer , Userserializer
from blog.models import Blog
# Create your views here.

class Apilist(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class DeleteApi(DestroyAPIView):
    queryset = Blog.objects.all()    
    serializer_class = BlogSerializer

class UpdateApi(UpdateAPIView):
    queryset = Blog.objects.all()    
    serializer_class = BlogSerializer

class RetrieveApi(RetrieveAPIView):
    queryset = Blog.objects.all()    
    serializer_class = BlogSerializer

class UserApiList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer