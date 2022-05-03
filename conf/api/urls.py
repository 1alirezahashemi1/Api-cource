from django.urls import *
from . views import Apilist
app_name = 'api'

urlpatterns = [
   path('',Apilist.as_view(),name='api')
]