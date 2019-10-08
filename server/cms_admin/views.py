import re, json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry,ADDITION,CHANGE,DELETION
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View, generic
from django.views.generic import DetailView, ListView, CreateView, edit
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.resolvers import RegexPattern, RoutePattern
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.core import serializers
from django.urls import reverse
from rest_framework.routers import DefaultRouter
from rest_framework import generics, viewsets
from cms import urls
from media_browser.models import *
from blog.models import *
from sites.models import *
from users.models import *
from .forms import *
from .models import *
from users.serializers import PermissionSerializer

# Create your views here.


def error_404_view(request, exception):
    template_name = "cms_admin/error/e404.html"
    data = {"name": "ThePythonDjango.com"}
    return render(request, template_name, data)


def get_new_contact_message():
    contacts = Contact.objects.filter(seen=False).order_by("-id")
    return contacts


def get_default_context(context,request):
    context["user"] = request.user.username
    context["contacts"] = get_new_contact_message()
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = None
    context["c_profile"] = profile
    return context

def get_logs_data(limit):
    return LogEntry.objects.all().order_by("-id")[:limit]

def store_log_info(request,model, flag):
    return LogEntry.objects.log_action(
    user_id         = request.user.id, 
    content_type_id = ContentType.objects.get_for_model(model).id,
    object_id       = model.id,
    object_repr     = "", 
    action_flag     = flag
)


class Error404Page(TemplateView):
    template_name = "cms_admin/error/e404.html"

    def get(self, request):
        context = {}
        response = render_to_response(
            self.template_name, context_instance=RequestContext(request)
        )
        response.status_code = 404
        return response
        # return render(request, self.template_name, context)


class LoginView(TemplateView):
    """docstring for LoginView."""

    template_name = "registration/login.html"

    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        print(self.kwargs)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/cms/admin/")

        return HttpResponseRedirect("/accounts/login/")

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/cms/admin/")


class LogoutView(TemplateView):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/accounts/login/")


class SiteView(generic.ListView):
    queryset = SiteInformation.objects.all().order_by("-id")
    template_name = "cms_admin/site/site.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = get_default_context(super().get_context_data(**kwargs), self.request)
        context["form"] = SiteForm()
        return context
    
    def post(self, request):
        try:
            form = SiteForm(request.POST)
            if form.is_valid():
                form.save()
                site = SiteInformation.objects.all()[0]
                store_log_info(request,site,1)
                messages.success(request, 'Site created successfully')
                return HttpResponseRedirect("/cms/site/")
        except:
            messages.error(request, 'Site not created!')
            return HttpResponseRedirect("/cms/site/")


class SiteUpdateView(TemplateView):

    template_name = "cms_admin/site/siteUpdate.html"

    def get(self, request, siteid):
        context = get_default_context({}, request)
        context["medias"] = MediaImage.objects.all()
        try:
            site = SiteInformation.objects.get(id=siteid)
            context["form"] = SiteForm(instance=site)
            context["site"] = site
            return render(request, self.template_name, context)
        except:
            messages.error(request, 'Server Error')
            return HttpResponseRedirect("/cms/site/")

    def post(self, request, siteid):
        try:
            site = SiteInformation.objects.get(id=siteid)
            if site:
                form = SiteForm(instance=site, data=request.POST)
                if form.is_valid():
                    form.save()
                    store_log_info(request,site,2)
                    messages.success(request, 'Site Information Updated')
                    return HttpResponseRedirect("/cms/site/")
        except:
            messages.success(request, 'Server Error')
            return HttpResponseRedirect("/cms/site/")


class SiteDeleteView(View):
    def get(self, request, siteid):
        try:
            site = SiteInformation.objects.get(id=siteid)
            store_log_info(request,site,3)
            site.delete()
            messages.warning(request, 'Site Information deleted. Add information for better experience')
            return HttpResponseRedirect("/cms/site/")
        except:
            messages.error(request, 'Server Error')
            return HttpResponseRedirect("/cms/site/")

class HomeView(TemplateView):
    template_name = "cms_admin/dashboard/dashboard.html"

    def get(self, request):
        context = get_default_context({}, request)
        context["total_user"] = User.objects.all().count()
        context["total_post"] = Post.objects.all().count()
        context["total_media"] = MediaImage.objects.all().count()
        context["new_message_count"] = Contact.objects.filter(seen=False).count()
        context["logs"] =  get_logs_data(10)
        return render(request, self.template_name, context)


class CategoryView(generic.ListView):
    queryset = Category.objects.all().order_by("-updated_at")
    template_name = "cms_admin/category/categoryList.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = get_default_context(super().get_context_data(**kwargs), self.request)
        form = CategoryForm()
        context["form"] = form
        return context


class CategoryAddView(TemplateView):
    template_name = "cms_admin/category/categoryAdd.html"

    def get(self, request):
        context = get_default_context({}, request)
        form = CategoryForm()
        context["form"] = form
        return render(request, self.template_name, context)

    def post(self, request):
        context = get_default_context({}, request)
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            cat = Category.objects.all().order_by("-created_at")[0]
            store_log_info(request,cat,1)
            messages.success(request, 'Category "{0}" created successfully'.format(cat.name))
            return HttpResponseRedirect("/cms/categories/")
        else:
            form = CategoryForm()
            context["user"] = request.user.username
            context["form"] = form
            context["contacts"] = get_new_contact_message()
            messages.error(request, 'Profile is not created!')
            return render(request, self.template_name, context)


class CategoryUpdateView(TemplateView):

    template_name = "cms_admin/category/categoryUpdate.html"

    def post(self, request, catid):
        context = get_default_context({}, request)
        try:
            category = Category.objects.get(id=catid)
            if category:
                form = CategoryForm(instance=category, data=request.POST)
                if form.is_valid():
                    form.save()
                    store_log_info(request,category,2)
                    messages.success(request, 'Category updated successfully'.format(category.name))
                    return HttpResponseRedirect("/cms/categories/")
        except:
            messages.error(request, 'Data is not valid')
            return HttpResponseRedirect("/cms/categories/{0}/change/".format(catid))

    def get(self, request, catid):
        context = get_default_context({}, request)
        try:
             category = Category.objects.get(id=catid)
             form = CategoryForm(instance=category)
             context["form"] = form
             context["category"] = category
             return render(request, self.template_name, context)
        except:
            form = CategoryForm()
            context["form"] = form
            return render(request, self.template_name, context)

class CategoryDeleteView(TemplateView):
    def get(self, request, catid):
        category = Category.objects.get(id=catid)
        if category:
            store_log_info(request,category,3)
            category.delete()
            return HttpResponseRedirect("/cms/categories/")


class TagListView(ListView):
    queryset = Tag.objects.all().order_by("-updated_at")
    template_name = "cms_admin/tag/tagList.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = get_default_context(super().get_context_data(**kwargs), self.request)
        form = TagForm()
        context["form"] = form

        return context


class TagAddView(TemplateView):
    template_name = "cms_admin/tag/tag_add.html"

    def get(self, request):
        context = get_default_context({}, request)
        form = TagForm()
        context["form"] = form
        return render(request, self.template_name, context)

    def post(self, request):
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            tag = Tag.objects.all().order_by("-created_at")[0]
            store_log_info(request,tag,1)
            messages.success(request, 'Tag "{0}" created successfully'.format(tag.name))
            return HttpResponseRedirect("/cms/tags/")
        else:
            messages.error(request, 'Tag is not created successfully'.format(tag.name))
            return HttpResponseRedirect("/cms/tags/")


class TagUpdateView(TemplateView):
    template_name = "cms_admin/tag/tagUpdate.html"

    def get(self, request, tagid):
        context = get_default_context({}, request)
        try:
            tag = Tag.objects.get(id=tagid)
            form = TagForm(instance=tag)
            context["form"] = form
            context["tag"] = tag
            return render(request, self.template_name, context)
        except:
            return HttpResponseRedirect("/cms/tags/")

        # if tag:

    def post(self, request, tagid):
        try:
            tag = Tag.objects.get(id=tagid)
            form = TagForm(instance=tag, data=request.POST)
            if form.is_valid():
                form.save()
                store_log_info(request,tag,2)
                messages.success(request, 'Tag "{0}" updated successfully'.format(tag.name))
                return HttpResponseRedirect("/cms/tags/")
            else:
                messages.error(request, 'Data is not valid')
                return HttpResponseRedirect("/cms/tags/{0}/change/".format(tagid))
        except:
            messages.error(request, 'Server Error')
            return HttpResponseRedirect("/cms/tags/{0}/change/".format(tagid))


class TagDeleteView(TemplateView):
    def get(self, request, tagid):
        tag = Tag.objects.get(id=tagid)
        if tag:
            store_log_info(request,tag,3)
            tag.delete()
            return HttpResponseRedirect("/cms/tags/")


class UserListView(ListView):
    template_name = "cms_admin/user/user.html"
    queryset = User.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = get_default_context(super().get_context_data(**kwargs), self.request)
        context["form"] = UserBasicForm()

        return context

    def post(self, request):
        form = UserBasicForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if len(form.email) == 0:
                messages.error(request, 'User email could not be empty')
                return HttpResponseRedirect("/cms/users/")
            else:
                form.set_password(form.password)
                form.save()
                user = User.objects.all().order_by("-id")[0]
                store_log_info(request,user,1)
                messages.success(request, 'User "{0}" created successfully'.format(user.username))
                return HttpResponseRedirect("/cms/users/")
        else:
            messages.error(request, 'Data is not valid')
            return HttpResponseRedirect("/cms/users/")




class ProfileView(TemplateView):
    template_name = "cms_admin/user/profile.html"

    def get(self, request, uid):
        context = get_default_context({}, request)
        user = User.objects.get(id=uid)
        form = UserForm(instance=user)
        context["form"] = form
        context["userobj"] = user
        context["social_form"] = SocialMediaForm()
        context["education_form"] = EducationForm()
        context["skill_form"] = SkillForm()
        context["password_form"] = UserPasswordForm()
        context["medias"] = MediaImage.objects.all()
        try:
            profile = Profile.objects.get(user=uid)
            if profile:
                context["profile"] = profile
                context["educations"] = profile.educations.all()
                context["skills"] = profile.skills.all()
                context["socialMedias"] = profile.socialMedias.all()
                context["profile_stage"] = "update"
                profile_form = ProfileForm(instance=profile)
                context["profile_form"] = profile_form
                context["profile_stage"] = "update"
                return render(request, self.template_name, context)
        except:
            profile_form = ProfileForm()
            context["profile_form"] = profile_form
            return render(request, self.template_name, context)


class ProfilePostView(View):
    def post(self, request, uid):
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            user = User.objects.get(id=uid)
            if user:
                profile.user = user
                profile = profile.save()
                profile = Profile.objects.all().order_by("-id")[0]
                store_log_info(request,profile,1)
                messages.success(request, 'Profile created successfully')
                return HttpResponseRedirect("/cms/users/{0}/profile".format(uid))


class ProfileUpdateView(View):
    def post(self, request, uid):
        profile = Profile.objects.get(user=uid)
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save()
            store_log_info(request,profile,2)
            messages.success(request, 'Profile updated successfully')
            return HttpResponseRedirect("/cms/users/{0}/profile".format(uid))


class UserUpdateView(View):
    def post(self, request, uid):
        user = User.objects.get(id=uid)
        form = UserForm(instance=user, data=request.POST)
        if form.is_valid():
            form = form.save()
            store_log_info(request,user,2)
            messages.success(request, 'User updated successfully')
            return HttpResponseRedirect("/cms/users/{0}/profile".format(uid))

class UserPasswordUpdateView(View):
    def post(self, request, uid):
        try:
            user = User.objects.get(id=uid)
            if user:
                form = UserPasswordForm(request.POST)
                if form.is_valid():
                    form = form.save(commit=False)
                    user.set_password(form.password)
                    user.save()
                    store_log_info(request,user,2)
                    messages.success(request, 'Password updated successfully')
                    return HttpResponseRedirect("/cms/users/{0}/profile".format(uid))

                else:
                    messages.error(request, 'password and confirm_password must be same')
                    return HttpResponseRedirect("/cms/users/{0}/profile".format(uid))

            else:
                messages.success(request, 'Server Error')
                return HttpResponseRedirect("/cms/users/")
        except:
            messages.success(request, 'Server Error')
            return HttpResponseRedirect("/cms/users/")

class EducationPostView(View):
    def post(self, request, uid):
        try:
            profile = Profile.objects.get(user=uid)
            if profile:
                form = EducationForm(request.POST)
                form = form.save(commit=False)
                form.profile = profile
                form = form.save()
                education = Education.objects.all().order_by("-id")[0]
                store_log_info(request,education,1)
                messages.success(request, 'Education created successfully')
                return HttpResponseRedirect("/cms/users/{0}/profile".format(uid))
            else:
                messages.error(request, 'Profile does not created yet')
                return HttpResponseRedirect("/cms/users/{0}/profile".format(uid))
        except:
            messages.error(request, 'Profile does not created yet')
            return HttpResponseRedirect("/cms/users/{0}/profile".format(uid))


class SocialPostView(View):
    def post(self, request, uid):
        try:
            profile = Profile.objects.get(user=uid)
            if profile:
                form = SocialMediaForm(request.POST)
                form = form.save(commit=False)
                form.profile = profile
                form = form.save()
                social = SocialMediaInfo.objects.all().order_by("-id")[0]
                store_log_info(request,social,1)
                messages.success(request, 'Social path saved successfully')
                return HttpResponseRedirect("/cms/users/{0}/profile".format(uid))
            else:
                messages.error(request, 'Profile does not created yet!')
                return HttpResponseRedirect("/cms/users/{0}/profile".format(uid))
        except:
            messages.error(request, 'Profile does not created yet')
            return HttpResponseRedirect("/cms/users/{0}/profile".format(uid))


class SkillPostView(View):
    def post(self, request, uid):
        try:
            profile = Profile.objects.get(user=uid)
            if profile:
                form = SkillForm(request.POST)
                form = form.save(commit=False)
                form.profile = profile
                form = form.save()
                skill = Skill.objects.all().order_by("-id")[0]
                store_log_info(request,skill,1)
                messages.success(request, 'Skill added successfully')
                return HttpResponseRedirect("/cms/users/{0}/profile".format(uid))
            else:
                messages.error(request, 'Profile does not created yet!')
                return HttpResponseRedirect("/cms/users/{0}/profile".format(uid))
        except:
            messages.error(request, 'Profile does not created yet')
            return HttpResponseRedirect("/cms/users/{0}/profile".format(uid))

class PostListView(ListView):
    queryset = Post.objects.all().order_by("-id")
    template_name = "cms_admin/post/postList.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = get_default_context(super().get_context_data(**kwargs), self.request)

        return context


class PostListAdminAPIView(View):
    def get(self, request):
        posts = (
            Post.objects.all()
            .order_by("-id")
            .values("id", "title", "category", "created_at")
        )
        # context["posts"] = posts

        return JsonResponse({"posts": list(posts)})


class PostAddView(TemplateView):

    template_name = "cms_admin/post/postAdd.html"

    def get(self, request):
        context = get_default_context({},request)
        context["form"] = PostForm()
        return render(request, self.template_name, context)

    def post(self, request):
        try:
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                post = Post.objects.all().order_by("-id")[0]
                store_log_info(request,post,1)
                messages.success(request, 'Post "{0}" created successfully'.format(post.title))
                return HttpResponseRedirect("/cms/posts/")
            else:
                messages.error(request, 'Post not created successfully')
                return HttpResponseRedirect("/cms/posts/add/")
        except:
            messages.error(request, 'Server error')
            return HttpResponseRedirect("/cms/posts/")


class PostUpdateView(TemplateView):
    template_name = "cms_admin/post/postAdd.html"

    def get(self, request, pid):
        context = get_default_context({},request)
        try:
            post = Post.objects.get(id=pid)
            form = PostForm(instance=post)
            context["form"] = form
            context["post"] = post
            context["stage"] = "update"
            return render(request, self.template_name, context)
        except:
            return HttpResponseRedirect("/cms/posts/")

    def post(self, request, pid):
        try:
            post = Post.objects.get(id=pid)
            form = PostForm(instance=post, data=request.POST)
            if form.is_valid():
                form.save()
                store_log_info(request,post,2)
                messages.success(request, 'Post "{0}" updated successfully'.format(post.title))
                return HttpResponseRedirect("/cms/posts/")
            else:
                messages.error(request, 'Validation error')
                return HttpResponseRedirect("/cms/posts/")
        except:
            messages.error(request, 'Server error')
            return HttpResponseRedirect("/cms/posts/")


class PostDeleteView(View):
    def get(self, request, pid):
        try:
            post = Post.objects.get(id=pid)
            if post:
                store_log_info(request,post,3)
                post.delete()
                messages.success(request, 'Post deleted successfully')
                return HttpResponseRedirect("/cms/posts/")
            else:
                messages.error(request, 'Data not found')
                return HttpResponseRedirect("/cms/posts/")
        except:
            messages.error(request, 'Server error')
            return HttpResponseRedirect("/cms/posts/")
        
        
def get_url_list(urls):
    url_list = []
    for index in range(0, len(urls), 4):
        url_text = (
            urls[index].pattern._regex
            if isinstance(urls[index].pattern, RegexPattern)
            else urls[index].pattern._route
        )
        url_text = re.sub("[^A-Za-z0-9]+", "", url_text)
        url_list.append(url_text)
    del url_list[-1]
    return url_list


class APIUrlListView(TemplateView):
    template_name = "cms_admin/api/apiList.html"

    def get(self, request):
        context = get_default_context({},request)
        public_urls = urls.public_router.get_urls()
        admin_urls = urls.admin_router.get_urls()
        context["public_urls"] = get_url_list(public_urls)
        return render(request, self.template_name, context)


class PermissionListView(ListView):
    queryset = Permission.objects.all()
    template_name = "cms_admin/permissions/permissionList.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = get_default_context(super().get_context_data(**kwargs), self.request)
        context["users"] = User.objects.all()
        context["user_roles"] = UserRole.objects.all().order_by("role")
        context["form"] = PermissionForm()
        return context

    def post(self, request):
        context = {}
        context["user"] = request.user.username
        form = PermissionForm(request.POST)

        if form.is_valid():
            form = PermissionForm(request.POST)
            if form.is_valid():
                new_permission = form.save()
                if new_permission:
                    return HttpResponseRedirect("/cms/permissions/")

        else:
            form = PermissionForm()
            context["user"] = request.user.username
            context["form"] = form
            context["form_error"] = "Data is not valid!"
            return render(request, self.template_name, context)


class PermissionRoleWiseListView(ListView):
    queryset = Permission.objects.all()
    template_name = "cms_admin/permissions/permissionList.html"
    paginate_by = 10

    def get_queryset(self):
        return UserRole.objects.get(id=self.kwargs["role_id"]).permissions.all()

    def get_context_data(self, **kwargs):
        context = get_default_context(super().get_context_data(**kwargs), self.request)
        context["users"] = User.objects.all()
        context["user_roles"] = UserRole.objects.all().order_by("role")
        context["form"] = PermissionForm()
        return context


class PermissionUpdateView(TemplateView):
    template_name = "cms_admin/permissions/permissionUpdate.html"

    def get(self, request, permission_id):
        try:
            context = get_default_context({}, request)
            permission = SystemPermission.objects.get(id=permission_id)
            form = PermissionForm(initial={"permission_name": permission.name})
            context["permission"] = permission
            context["form"] = form
            return render(request, self.template_name, context)
        except:
            return HttpResponseRedirect("/cms/permissions/")

    def post(self, request, permission_id):
        form = PermissionForm(request.POST)
        if form.is_valid():
            permissionValue = form.cleaned_data["permission_name"]
            permission = SystemPermission.objects.get(id=permission_id)
            if len(permissionValue) > 0:
                permission.name = permissionValue
                permission.save()
                return HttpResponseRedirect("/cms/permissions/")


class PermissionDeleteView(TemplateView):
    def get(self, request, permission_id):
        permission = SystemPermission.objects.get(id=permission_id)
        if permission:
            permission.delete()
            return HttpResponseRedirect("/cms/permissions/")


class MenuItemView(TemplateView):
    template_name = "cms_admin/menu/menuAdd.html"

    def get(self, request):
        context = get_default_context({},request)
        context["form"] = MenuForm()
        menus = MenuItem.objects.order_by("-id")
        context["menus"] = menus

        return render(request, self.template_name, context)

    def post(self, request):
        try:
            form = MenuForm(request.POST)
            if form.is_valid():
                form.save()
                menu = MenuItem.objects.all().order_by("-id")[0]
                store_log_info(request,menu,1)
                messages.success(request, 'Menu created successfully')
                return HttpResponseRedirect("/cms/menus/")
        except:
            messages.error(request, 'Server error/Site is not created')
            return HttpResponseRedirect("/cms/menus/")
            
            
        
class MenuItemUpdateView(TemplateView):
    template_name = "cms_admin/menu/menuUpdate.html"

    def get(self, request, mid):
        context = get_default_context({}, request)
        try:
            menu = MenuItem.objects.get(id=mid)
            context["form"] = MenuForm(instance=menu)
            context["menu"] = menu
            return render(request, self.template_name, context)
        except:
            messages.error(request, 'Server error')
            return HttpResponseRedirect("/cms/menus/")
        
        
    def post(self, request, mid):
        try:
            menu = MenuItem.objects.get(id=mid)
            form = MenuForm(instance=menu, data=request.POST)
            if form.is_valid():
                form.save()
                store_log_info(request,menu,2)
                menu = MenuItem.objects.get(id=mid)
                messages.success(request, 'Menu "{0}" Updated'.format(menu.name))
                return HttpResponseRedirect("/cms/menus/")
        except:
            messages.error(request, 'Server Error')
            return HttpResponseRedirect("/cms/menus/")


class MenuItemDeleteView(View):
    def get(self, request, mid):
        try:
            menu = MenuItem.objects.get(id=mid)
            if menu:
                menu_name = menu.name 
                store_log_info(request,menu,3)
                menu.delete()
                messages.success(request, 'Menu "{0}" deleted'.format(menu_name))
                return HttpResponseRedirect("/cms/menus/")
        except:
            messages.error(request, 'Server Error')
            return HttpResponseRedirect("/cms/menus/")


class MediaBrowserView(ListView):
    queryset = MediaImage.objects.all().order_by("-id")
    template_name = "cms_admin/media/mediaList.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = get_default_context(super().get_context_data(**kwargs), self.request)
        context["form"] = MediaBrowserForm()

        return context

    def post(self, request):
        form = MediaBrowserForm(request.POST, request.FILES)
        if form.is_valid():
            new_media = form.save(commit=False)
            new_media.owner = request.user
            new_media.save()
            media = MediaImage.objects.all().order_by("-id")[0]
            store_log_info(request,media,1)
            messages.success(request, 'New media image created successfully')
            return HttpResponseRedirect("/cms/medias/")


class MediaBrowserUpdateView(TemplateView):
    template_name = "cms_admin/media/mediaUpdate.html"

    def get(self, request, mid):
        context = get_default_context({},request)
        media = MediaImage.objects.get(id=mid)
        context["media"] = media
        context["media_size"] = media.image.size * (10 ** -6)
        form = MediaBrowserForm(instance=media)
        form.image = None
        context["form"] = form

        return render(request, self.template_name, context)
    

    def post(self, request, mid):
        try:
            media = MediaImage.objects.get(id=mid)
            form = MediaBrowserForm(instance=media, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Image updated successfully')
                store_log_info(request,media,2)
                return HttpResponseRedirect("/cms/medias/")
        except:
            messages.error(request, 'Server Error')
            return HttpResponseRedirect("/cms/medias/{0}/change/".format(mid))


class MediaDeleteView(View):
    def get(self, request, mid):
        try:
            media = MediaImage.objects.get(id=mid)
            if media:
                store_log_info(request,media,3)
                media.delete()
                return HttpResponseRedirect("/cms/medias/")

        except:
            messages.error(request, 'Server Error')
            return HttpResponseRedirect("/cms/medias/{0}/change/".format(mid))

class ContactListView(TemplateView):
    template_name = "cms_admin/contact/contactList.html"

    def get(self, request):
        context = get_default_context({},request)
        context["contact_list"] = Contact.objects.all().order_by("-id")

        return render(request, self.template_name, context)


class ContactView(TemplateView):
    template_name = "cms_admin/contact/contact-view.html"

    def get(self, request, cid):
        context = get_default_context({},request)
        contact = Contact.objects.get(id=cid)
        if contact.seen is False:
            contact.seen = True
            contact.save()
        context["contact"] = contact

        return render(request, self.template_name, context)


class ContactDeleteView(TemplateView):
    def get(self, request, cid):
        try:
            contact = Contact.objects.get(id=cid)
            store_log_info(request,contact,3)
            contact.delete()
            return HttpResponseRedirect("/cms/contacts/")
        except:
            return HttpResponseRedirect("/cms/contacts/")



