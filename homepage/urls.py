from django.urls import path
from . import views
from .views import login_user, register_user

urlpatterns = [
    path('', views.homepage, name="home"),
    path('home/', views.homepage, name="homepage"),
    path('testhome/', views.testhome, name="testhome"),
    path('login_user/', login_user, name="loginuser"),
    path('register_user/', register_user, name="registeruser"),


]