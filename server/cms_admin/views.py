from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.views.generic import TemplateView, View
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import *
from sites.models import *
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
        

class SiteView(TemplateView):
    template_name = "cms_admin2/site/site.html"

    def get(self, request):
        context = {}
        context["user"] = request.user.username
        try:
           site = SiteInformation.objects.all()[0]
           context["site"] = site
           site_data = {
               "site_name": site.site_name
           }
           form = SiteForm(initial=site_data)
           context["form"] = form

           return render(request, self.template_name, context)
        except :
            form = SiteForm()
            context["form"] = form
            return render(request, self.template_name, context)
        
        

class SiteUpdateView(TemplateView):

    template_name = "cms_admin2/site/site.html"

    def post(self, request, siteid):
        context = {}
        context['user'] = request.user.username
        form = SiteForm(request.POST)
        if form.is_valid():
            siteValue = form.cleaned_data['site_name']
            site = SiteInformation.objects.get(id=siteid)
            if len(siteValue) > 0:
                site.site_name = siteValue
                site.save()
                return HttpResponseRedirect('/cms/site/')
            else:
                return HttpResponseRedirect('/cms/site/')

        else:
            form = SiteForm()
            context['user'] = request.user.username
            context['form'] = form
            return render(request, self.template_name, context)

class HomeView(TemplateView):
    template_name = "cms_admin2/dashboard/dashboard.html"

    def get(self, request):
        return render(request, self.template_name, {"user": request.user.username})


class ProfileView(TemplateView):
    template_name = "cms_admin/profile.html"

class CategoryView(TemplateView):
    template_name = "cms_admin2/category/categoryList.html"

    def get(self, request):
        context = {}
        categories = Category.objects.all().order_by('-updated_at')
        context['user'] = request.user.username
        context['categories'] = categories
        form = CategoryForm()
        context['form'] = form
        return render(request, self.template_name, context)


class CategoryAddView(TemplateView):
    template_name = "cms_admin2/category/categoryAdd.html"

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
                return HttpResponseRedirect('/cms/categories/')
        else:
            form = CategoryForm()
            context['user'] = request.user.username
            context['form'] = form
            context['form_error'] = "Data is not valid!"
            return render(request, self.template_name, context)



class CategoryUpdateView(TemplateView):

    template_name = "cms_admin2/category/categoryUpdate.html"

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
                return HttpResponseRedirect('/cms/categories/')
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
            return HttpResponseRedirect('/cms/categories/')


class TagListView(TemplateView):
    template_name = "cms_admin2/tag/tagList.html"

    def get(self, request):
        tags = Tag.objects.all().order_by('-updated_at')
        context = {}
        context['tags'] = tags
        context['user'] = request.user.username
        form = TagForm()
        context['form'] = form

        return render(request, self.template_name, context)


class TagAddView(TemplateView):
    template_name = "cms_admin/tag/tag_add.html"

    def get(self, request):
        context = {}
        context['user'] = request.user.username
        form = TagForm()
        context['form'] = form

        return render(request, self.template_name, context)

    
    def post(self,request):
        context = {}
        context['user'] = request.user.username
        form = TagForm(request.POST)
        if form.is_valid():
            tagValue = form.cleaned_data['tag']
            if len(tagValue) == 0:
                form = TagForm()
                context['user'] = request.user.username
                context['form'] = form
                context['form_error'] = "You can not submit empty field!"
                return render(request, self.template_name, context)
            else:
                tagObj = Tag(name=tagValue)
                tagObj.save()
                return HttpResponseRedirect('/cms/tags/')
        else:
            form = TagForm()
            context['user'] = request.user.username
            context['form'] = form
            context['form_error'] = "Data is not valid!"
            return render(request, self.template_name, context)


class TagUpdateView(TemplateView):
    template_name = "cms_admin2/tag/tagUpdate.html"

    def get(self, request, tagid):
        context = {}
        try:
            tag = Tag.objects.get(id=tagid)
            form = TagForm(initial={'tag': tag.name})
            context['tag'] = tag
            context['user'] = request.user.username
            context['form'] = form
            return render(request, self.template_name, context)
        except:
            return HttpResponseRedirect('/cms/tags/')
        
        # if tag:
        
    
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

class TagDeleteView(TemplateView):

    def get(self, request, tagid):
        tag = Tag.objects.get(id=tagid)
        if tag:
            tag.delete()
            return HttpResponseRedirect('/cms/tags/')

class MediaListView(TemplateView):
    template_name = "cms_admin2/media/mediaList.html"

    def get(self, request):
        context = {}
        context["user"] = request.user.username

        return render(request, self.template_name, context)

class UserListView(TemplateView):
    template_name = "cms_admin2/user/user.html"

    def get(self, request):
        users = User.objects.all()
        context = {}
        context["user"] = request.user.username
        context["users"] = users

        return render(request, self.template_name, context) 


class ProfileView(TemplateView):
    template_name = "cms_admin2/user/profile.html"

    def get(self, request, uid):
        context = {}
        userobj = User.objects.get(id=uid)
        context["user"] = request.user.username
        context["userobj"] = userobj
        context["educations"] = userobj.profile.educations.all().order_by("id")
        context["skills"] = userobj.profile.skills.all()
        context["socialMedias"] = userobj.profile.socialMedias.all().order_by("id")
        user_data = {
            'first_name':userobj.first_name,
            'last_name':userobj.last_name,
            'email':userobj.email,
            'mobile':userobj.profile.mobile,
            'bio':userobj.profile.bio,
            'about':userobj.profile.about,
        }
        user_form = UserForm(initial=user_data)
        context["user_form"] = user_form

        return render(request, self.template_name, context) 


class PostListView(TemplateView):
    template_name  = "cms_admin2/post/postList.html"

    def get(self, request):
        context = {}
        context["user"] = request.user.username
        context["posts"] = Post.objects.all().order_by("id")

        return render(request, self.template_name, context)
    

class PostAddView(TemplateView):
    template_name = "cms_admin2/post/postAdd.html"

    def get(self, request):
        context = {}
        context["user"] = request.user.username
        context["categories"] = Category.objects.all().order_by("id")
        context["tags"] = Tag.objects.all().order_by("id")
        return render(request,  self.template_name, context)
