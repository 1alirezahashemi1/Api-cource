from django.urls import *
from . views import  Apilist , UserApiList ,DeleteApi, RetrieveApi , UpdateApi
app_name = 'api'

urlpatterns = [
   path('',Apilist.as_view(),name='api'),
 
   path('<int:pk>/delete',DeleteApi.as_view(),name='delete-api'),
   path('<int:pk>/retrieve',RetrieveApi.as_view(),name='retrieve'),
   path('<int:pk>/update',UpdateApi.as_view(),name='api-update'),
   path("users/",UserApiList.as_view(),name='user-api-list'),
]