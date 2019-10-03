from django import forms
from django.contrib.auth.models import User, Permission
from django.forms import ModelForm, Form
from blog.models import *
from sites.models import *
from users.models import *
from media_browser.models import *


def get_category_list():
    data = []
    for cat in Category.objects.all():
        data.append((cat.id, cat.name))
    data = tuple(data)
    return


class CategoryForm(Form):
    category = forms.CharField(label="Category", max_length=100)

    def clean_category(self):
        data = self.cleaned_data["category"]
        return data


class TagForm(Form):
    tag = forms.CharField(label="Tag", max_length=100)

    def clean_category(self):
        data = self.cleaned_data["tag"]
        return data


class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["body"].widget.attrs["rows"] = "5"
        self.fields["category"].widget.attrs["class"] = "form-control custom-select"
        self.fields["tags"].widget.attrs["class"] = "custom-select"
        self.fields["published"].widget.attrs["class"] = "custom-select"

    class Meta:
        model = Post
        fields = ["title", "subtitle", "body", "category", "tags", "published"]


class PermissionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PermissionForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["content_type"].widget.attrs["class"] = "form-control custom-select"
        self.fields["codename"].widget.attrs["class"] = "form-control"

    class Meta:
        model = Permission
        fields = ["name", "content_type", "codename"]


class UserBasicForm(Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.CharField(label="Email")
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password")


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["is_superuser"].widget.attrs["class"] = "form-check-input"

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "is_superuser"]


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields["bio"].widget.attrs["class"] = "form-control"
        self.fields["about"].widget.attrs["rows"] = "5"
        self.fields["mobile"].widget.attrs["class"] = "form-control"
        self.fields["user_role"].widget.attrs["class"] = "form-control custom-select"

    class Meta:
        model = Profile
        fields = ["avatar", "bio", "about", "mobile", "user_role"]


class SocialMediaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SocialMediaForm, self).__init__(*args, **kwargs)
        self.fields["type"].widget.attrs["class"] = "form-control custom-select"
        self.fields["url"].widget.attrs["class"] = "form-control"

    class Meta:
        model = SocialMediaInfo
        fields = ["type", "url"]


class SiteForm(Form):
    site_name = forms.CharField(label="Site Name", max_length=120)


class MenuForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["url"].widget.attrs["class"] = "form-control"
        self.fields["allow_submenu"].widget.attrs["class"] = "custom-select"
        self.fields["parent_menu"].widget.attrs["class"] = "custom-select"

    class Meta:
        model = MenuItem
        fields = ["name", "url", "allow_submenu", "parent_menu"]


class MediaBrowserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MediaBrowserForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs["class"] = "form-control"
        self.fields["height"].widget.attrs["class"] = "form-control"
        self.fields["width"].widget.attrs["class"] = "form-control"
        self.fields["image"].widget.attrs["class"] = "custom-file-input"

    class Meta:
        model = MediaImage
        fields = ["title", "height", "width", "image"]

