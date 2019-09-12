from django.shortcuts import render
from django.views.generic import TemplateView 
# Create your views here.

class LoginView(TemplateView):
    """docstring for LoginView."""
    template_name = "login.html"
        


class HomeView(TemplateView):
    template_name = "index.html"
        
