from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, View
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import * 
from .forms import *
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


class LogoutView(TemplateView):
    
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/accounts/login/')
        


class HomeView(TemplateView):
    template_name = "cms_admin/dashboard.html"

    def get(self, request):
        return render(request, self.template_name, {"user": request.user.username})


class ProfileView(TemplateView):
    template_name = "cms_admin/profile.html"

class CategoryView(TemplateView):
    template_name = "cms_admin/category.html"

    def get(self, request):
        context = {}
        categories = Category.objects.all()
        context['user'] = request.user.username
        context['categories'] = categories
        return render(request, self.template_name, context)

class CategoryUpdateView(TemplateView):

    template_name = "cms_admin/category_update.html"

    def post(self, request, catid):
        print("working")
        context = {}
        context['user'] = request.user.username
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = Category.objects.get(id=catid)
            category.name = form.cleaned_data['category']
            category.save()
            return HttpResponseRedirect('/cms/admin/')
        else:
            form = CategoryForm()
            return render(request, self.template_name, context)


    def get(self, request, catid):
        context = {}
        category = Category.objects.get(id=catid)
        form = CategoryForm(initial={'category': category.name})
        context['user'] = request.user.username
        context['category'] = category
        context['form'] = form

        return render(request, self.template_name, context)
        
