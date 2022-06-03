from rest_framework.generics import *
from django.contrib.auth import get_user_model
from rest_framework.permissions import * 
from . permissions import *
from rest_framework.permissions import BasePermission
from .serializers import BlogSerializer , Userserializer
from blog.models import Blog
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class ArticleViesSet(ModelViewSet):
  
    serializer_class = BlogSerializer

    def get_permissions(self):
        if self.action in ['list','create']:
            permission_classes = [IsStafforReadOnly]
        else:
            permission_classes = [IsAuthororReadonly]
        return [permission() for permission in permission_classes]


    def get_queryset(self):
     
        queryset = Blog.objects.all()
        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


class UserApiList(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = Userserializer
    permission_classes =  [IssuperUserOrStaffreadOnly]


    

    
