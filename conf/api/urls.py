from django.urls import *
from rest_framework import routers
from . views import  ArticleViesSet , UserApiList 
app_name = 'api'

router = routers.SimpleRouter()
router.register('', ArticleViesSet,basename='article')

urlpatterns = [
   path('',include(router.urls))
]