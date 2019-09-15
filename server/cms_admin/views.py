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
        categories = Category.objects.all().order_by('-updated_at')
        context['user'] = request.user.username
        context['categories'] = categories
        return render(request, self.template_name, context)


class CategoryAddView(TemplateView):
    template_name = "cms_admin/category_add.html"

    def get(self, request):
        context = {}
        form = CategoryForm()
        context['user'] = request.user.username
        context['form'] = form

        return render(request, self.template_name, context)

    def post(self, request):
        context = {}
        form = CategoryForm(request.POST)
        if form.is_valid():
            catValue = form.cleaned_data['category']
            if len(catValue) == 0:
                form = CategoryForm()
                context['user'] = request.user.username
                context['form'] = form
                context['form_error'] = "You can not submit empty field!"
                return render(request, self.template_name, context)
            else:
                catObj = Category(name=catValue)
                catObj.save()
                return HttpResponseRedirect('/cms/category/')
        else:
            form = CategoryForm()
            context['user'] = request.user.username
            context['form'] = form
            context['form_error'] = "Data is not valid!"
            return render(request, self.template_name, context)



class CategoryUpdateView(TemplateView):

    template_name = "cms_admin/category_update.html"

    def post(self, request, catid):
        context = {}
        context['user'] = request.user.username
        form = CategoryForm(request.POST)
        if form.is_valid():
            catValue = form.cleaned_data['category']
            category = Category.objects.get(id=catid)
            if len(catValue) > 0:
                category.name = catValue
                category.save()
                return HttpResponseRedirect('/cms/category/')
            else:
                form = CategoryForm(initial={'category': category.name})
                context['user'] = request.user.username
                context['category'] = category
                context['form'] = form
                return render(request, self.template_name, context)

        else:
            form = CategoryForm()
            return render(request, self.template_name, context)


    def get(self, request, catid):
        context = {}
        category = Category.objects.get(id=catid)
        if category:
            form = CategoryForm(initial={'category': category.name})
            context['user'] = request.user.username
            context['category'] = category
            context['form'] = form

            return render(request, self.template_name, context)
        

class CategoryDeleteView(TemplateView):

    def get(self, request, catid):
        category = Category.objects.get(id=catid)
        if category:
            category.delete()
            return HttpResponseRedirect('/cms/category/')


class TagListView(TemplateView):
    template_name = "cms_admin/tag/tag.html"

    def get(self, request):
        tags = Tag.objects.all().order_by('-updated_at')
        context = {}
        context['tags'] = tags
        context['user'] = request.user.username

        return render(request, self.template_name, context)


class TagUpdateView(TemplateView):
    template_name = "cms_admin/tag/tag_update.html"

    def get(self, request, tagid):
        tag = Tag.objects.get(id=tagid)
        context = {}
        # if tag:
        form = TagForm(initial={'tag': tag.name})
        context['tag'] = tag
        context['user'] = request.user.username
        context['form'] = form
        return render(request, self.template_name, context)
    
    def post(self, request, tagid):
        context = {}
        form = TagForm(request.POST)
        if form.is_valid():
            tagValue = form.cleaned_data['tag']
            tag = Tag.objects.get(id=tagid)
            if len(tagValue) > 0:
                tag.name = tagValue
                tag.save()
                return HttpResponseRedirect('/cms/tags/')



