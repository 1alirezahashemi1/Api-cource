from django.urls import *
from . views import  Apilist , UserApiList , retrieveUpdatedelete_blog
app_name = 'api'

urlpatterns = [
   path('',Apilist.as_view(),name='api'),
   path('<int:pk>',retrieveUpdatedelete_blog.as_view(),name='rdu_blog'),
   path("users/<int:pk>",UserApiList.as_view(),name='user-api-list'),
]