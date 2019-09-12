from django.contrib import admin 
from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('admin/', HomeView.as_view(), name="home"),
]