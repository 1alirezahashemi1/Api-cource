from django.contrib import admin
from django.urls import path , include
from blog. views import *
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('api/',include('api.urls')),
    path('api/token-auth/',ObtainAuthToken.as_view()),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),


]
