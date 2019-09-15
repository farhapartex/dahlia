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
    path('tags/', login_required(TagListView.as_view()), name="tags"),
    path('tags/add/', login_required(TagAddView.as_view()), name="tag_add"),
    path('tags/<int:tagid>/change/', login_required(TagUpdateView.as_view()), name="tag_update"),
    path('tags/<int:tagid>/delete/', login_required(TagDeleteView.as_view()), name="tag_delete"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]