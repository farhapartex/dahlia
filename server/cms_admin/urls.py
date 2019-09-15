from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('admin/', login_required(HomeView.as_view()), name="home"),
    path('profile/', login_required(ProfileView.as_view()), name="profile"),
    path('category/<int:catid>/change/', login_required(CategoryUpdateView.as_view()), name="category_update"),
    path('category/add/', login_required(CategoryAddView.as_view()), name="category_add"),
    path('category/<int:catid>/delete/', login_required(CategoryDeleteView.as_view()), name="category_delete"),
    path('category/', login_required(CategoryView.as_view()), name="category"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]