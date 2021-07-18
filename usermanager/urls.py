from django.urls import path
from . import views

urlpatterns = [
    path('register',views.RenderSignup),
    path('login',views.RenderLogin),
    path('logmeout',views.logoutview),
    path('generateotp',views.sendOtp),
    path('verify/register',views.RegisterUser),
    path('login/verify',views.loginuser),
]