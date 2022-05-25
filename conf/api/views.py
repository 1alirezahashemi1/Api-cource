from rest_framework.generics import *
from django.contrib.auth.models import User
from rest_framework.permissions import * 
from . permissions import *
from rest_framework.permissions import BasePermission
from .serializers import BlogSerializer , Userserializer
from blog.models import Blog
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class Apilist(ListCreateAPIView):
    queryset = Blog.objects.filter(status = True)
    serializer_class = BlogSerializer
    
class retrieveUpdatedelete_blog(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [ IsAuthororReadonly]
    

class UserApiList(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes =  [IssuperUserOrStaffreadOnly]

class RevokeToken(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self,request):
        request.auth.delete()
        return Response({"msg":"deleted"},status=204)
    
