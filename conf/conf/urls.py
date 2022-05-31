from django.contrib import admin
from django.urls import path , include
from blog. views import *
from rest_framework.authtoken.views import ObtainAuthToken
from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView,
    PasswordResetView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('api/',include('api.urls')),
    path('api/token-auth/',ObtainAuthToken.as_view()),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]
