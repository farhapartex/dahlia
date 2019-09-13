from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, View
from django.http import HttpResponse,HttpResponseRedirect  
# Create your views here.

class LoginView(TemplateView):
    """docstring for LoginView."""
    template_name = "registration/login.html"
    def post(self, request):
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        print(self.kwargs)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/cms/admin/') 
        
        return HttpResponseRedirect('/accounts/login/')
    
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/cms/admin/')

        print(resquest.GET.get('next',''))


class LogoutView(TemplateView):
    
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/accounts/login/')
        


class HomeView(TemplateView):
    template_name = "admin/dashboard.html"
        
