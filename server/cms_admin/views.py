from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.views.generic import TemplateView, View
from django.http import HttpResponse,HttpResponseRedirect
from django.urls.resolvers import RegexPattern,RoutePattern
from rest_framework.routers import DefaultRouter
import re
from cms import urls
from blog.models import *
from sites.models import *
from .forms import *
from .models import *
# Create your views here.

def error_404_view(request, exception):
    template_name = "cms_admin/error/e404.html"
    data = {"name": "ThePythonDjango.com"}
    return render(request,template_name, data)


class Error404Page(TemplateView):
    template_name = "cms_admin/error/e404.html"

    def get(self, request):
        context = {}
        response = render_to_response(self.template_name,context_instance=RequestContext(request))
        response.status_code = 404
        return response
        # return render(request, self.template_name, context)

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
    template_name = "cms_admin/site/site.html"

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

    template_name = "cms_admin/site/site.html"

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
    template_name = "cms_admin/dashboard/dashboard.html"

    def get(self, request):
        context= {}
        context["user"] = request.user.username
        context["total_user"] = User.objects.all().count()
        context["total_post"] = Post.objects.all().count()
        return render(request, self.template_name, context)


class CategoryView(TemplateView):
    template_name = "cms_admin/category/categoryList.html"

    def get(self, request):
        context = {}
        categories = Category.objects.all().order_by('-updated_at')
        context['user'] = request.user.username
        context['categories'] = categories
        form = CategoryForm()
        context['form'] = form
        return render(request, self.template_name, context)


class CategoryAddView(TemplateView):
    template_name = "cms_admin/category/categoryAdd.html"

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

    template_name = "cms_admin/category/categoryUpdate.html"

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
    template_name = "cms_admin/tag/tagList.html"

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
    template_name = "cms_admin/tag/tagUpdate.html"

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
    template_name = "cms_admin/media/mediaList.html"

    def get(self, request):
        context = {}
        context["user"] = request.user.username

        return render(request, self.template_name, context)
        


class UserListView(TemplateView):
    template_name = "cms_admin/user/user.html"

    def get(self, request):
        users = User.objects.all()
        context = {}
        context["user"] = request.user.username
        context["form"] = UserBasicForm()
        context["users"] = users

        return render(request, self.template_name, context) 

    def post(self, request):
        context = {}
        context['user'] = request.user.username
        form = UserBasicForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if len(first_name) == 0 or len(last_name) == 0 or len(email) == 0 or len(username) == 0 or len(password)==0:
                form = UserBasicForm()
                context['user'] = request.user.username
                context['form'] = form
                context['form_error'] = "You can not submit empty field!"
                return render(request, self.template_name, context)
            else:
                user = User.objects.create_user(username, email, password)
                user.first_name=first_name
                user.last_name =last_name
                user.save()
                return HttpResponseRedirect('/cms/users/')
        else:
            form = UserBasicForm()
            context['user'] = request.user.username
            context['form'] = form
            context['form_error'] = "Data is not valid!"
            return render(request, self.template_name, context)


class ProfileView(TemplateView):
    template_name = "cms_admin/user/profile.html"

    def get(self, request, uid):
        context = {}
        context["user"] = request.user.username
        try:
            userobj = User.objects.get(id=uid)
            context["userobj"] = userobj
            user_data = {
                'first_name':userobj.first_name,
                'last_name':userobj.last_name,
                'email':userobj.email,
            }
            if userobj.is_superuser:
                user_data["mobile"] = userobj.profile.mobile
                user_data["bio"] = userobj.profile.bio
                user_data["about"] = userobj.profile.about
                context["educations"] = userobj.profile.educations.all().order_by("id")
                context["skills"] = userobj.profile.skills.all()
                context["socialMedias"] = userobj.profile.socialMedias.all().order_by("id")

            user_form = UserForm(initial=user_data)
            context["user_form"] = user_form
        except:
            user_form = UserForm()
            context["user_form"] = user_form
        

        return render(request, self.template_name, context) 


class PostListView(TemplateView):
    template_name  = "cms_admin/post/postList.html"

    def get(self, request):
        context = {}
        context["user"] = request.user.username
        context["posts"] = Post.objects.all().order_by("-id")

        return render(request, self.template_name, context)
    

class PostAddView(TemplateView):
    template_name = "cms_admin/post/postAdd.html"

    def get(self, request):
        context = {}
        context["user"] = request.user.username
        form = PostForm()
        context["form"] = form
        return render(request,  self.template_name, context)
    
    def post(self, request):
        context = {}
        context["user"] = request.user.username
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            if new_post:
                return HttpResponseRedirect('/cms/posts/')



class PostUpdateView(TemplateView):
    template_name = "cms_admin/post/postAdd.html"

    def get(self, request, pid):
        context = {}
        context["user"] = request.user.username
        try:
            post = Post.objects.get(id=pid)
            form = PostForm(instance=post)
            context["form"] = form
            context["stage"] = "update"
            return render(request, self.template_name, context)
        except:
            return HttpResponseRedirect('/cms/posts/')
            



class APIUrlListView(TemplateView):
    template_name = "cms_admin/api/apiList.html"

    def get(self, request):
        context = {}
        context["user"] = request.user.username
        url_list = []
        all_url = urls.public_router.get_urls()

        for url_indx in range(0, len(all_url),4):
            url_txt = all_url[url_indx].pattern._regex if isinstance(all_url[url_indx].pattern, RegexPattern) else uall_url[url_indx].pattern._route
            url_txt = re.sub('[^A-Za-z0-9]+', '', url_txt)
            url_list.append(url_txt)
        del url_list[-1]
        context["url_list"] = url_list
        return render(request, self.template_name, context)


class PermissionListView(TemplateView):
    template_name = "cms_admin/permissions/permissionList.html"

    def get(self, request):
        context = {}
        context["user"] = request.user.username
        permissions = SystemPermission.objects.all().order_by("-id")
        context["permissions"] = permissions
        context["form"] = PermissionForm()
        return render(request, self.template_name, context)
        
    def post(self, request):
        context = {}
        context['user'] = request.user.username
        form = PermissionForm(request.POST)

        if form.is_valid():
            permission_name = form.cleaned_data['permission_name']
            if len(permission_name) == 0:
                form = PermissionForm()
                context['user'] = request.user.username
                context['form'] = form
                context['form_error'] = "You can not submit empty field!"
                return render(request, self.template_name, context)
            else:
                permissionObj = SystemPermission(name=permission_name)
                permissionObj.save()
                return HttpResponseRedirect('/cms/permissions/')
        else:
            form = PermissionForm()
            context['user'] = request.user.username
            context['form'] = form
            context['form_error'] = "Data is not valid!"
            return render(request, self.template_name, context)


class PermissionUpdateView(TemplateView):
    template_name = "cms_admin/permissions/permissionUpdate.html"

    def get(self, request, permission_id):
        try:
            context = {}
            permission = SystemPermission.objects.get(id=permission_id)
            form = PermissionForm(initial={'permission_name': permission.name})
            context['permission'] = permission
            context['user'] = request.user.username
            context['form'] = form
            return render(request, self.template_name, context)
        except:
            return HttpResponseRedirect('/cms/permissions/')

    def post(self, request, permission_id):
        context = {}
        form = PermissionForm(request.POST)
        if form.is_valid():
            permissionValue = form.cleaned_data['permission_name']
            permission = SystemPermission.objects.get(id=permission_id)
            if len(permissionValue) > 0:
                permission.name = permissionValue
                permission.save()
                return HttpResponseRedirect('/cms/permissions/')
        

class PermissionDeleteView(TemplateView):

    def get(self, request, permission_id):
        permission = SystemPermission.objects.get(id=permission_id)
        if permission:
            permission.delete()
            return HttpResponseRedirect('/cms/permissions/')