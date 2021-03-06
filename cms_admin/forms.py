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


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control"

    class Meta:
        model = Category
        fields = ["name"]


class TagForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control"

    class Meta:
        model = Tag
        fields = ["name"]


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


class UserBasicForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserBasicForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username","password"]


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]


class UserPasswordForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserPasswordForm, self).__init__(*args, **kwargs)
        self.fields["password"].widget.attrs["class"] = "form-control"
        self.fields["confirm_password"].widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ["password", "confirm_password"]

    def clean(self):
        cleaned_data = super(UserPasswordForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields["bio"].widget.attrs["class"] = "form-control"
        self.fields["about"].widget.attrs["rows"] = "5"
        self.fields["mobile"].widget.attrs["class"] = "form-control"
        self.fields["avatar"].widget.attrs["class"] = "form-control custom-select hide"
        self.fields["user_role"].widget.attrs["class"] = "form-control custom-select"

    class Meta:
        model = Profile
        fields = ["avatar", "bio", "about", "mobile", "avatar", "user_role"]


class SocialMediaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SocialMediaForm, self).__init__(*args, **kwargs)
        self.fields["type"].widget.attrs["class"] = "form-control custom-select"
        self.fields["url"].widget.attrs["class"] = "form-control"

    class Meta:
        model = SocialMediaInfo
        fields = ["type", "url"]


class EducationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        self.fields["degree"].widget.attrs["class"] = "form-control"
        self.fields["institution"].widget.attrs["class"] = "form-control"
        self.fields["session"].widget.attrs["class"] = "form-control"

    class Meta:
        model = Education
        fields = ["degree", "institution", "session"]


class SkillForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control"

    class Meta:
        model = Skill
        fields = ["name"]


class SiteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SiteForm, self).__init__(*args, **kwargs)
        self.fields["site_name"].widget.attrs["class"] = "form-control"
        self.fields["site_logo"].widget.attrs["class"] = "form-control custom-select hide"
        self.fields["site_favicon"].widget.attrs["class"] = "form-control custom-select hide"

    class Meta:
        model = SiteInformation
        fields = ["site_name","site_logo","site_favicon"]


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
        self.fields["image"].widget.attrs["class"] = "form-control-file"

    class Meta:
        model = MediaImage
        fields = ["title", "height", "width", "image"]


class UserRoleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserRoleForm, self).__init__(*args, **kwargs)
        self.fields["role"].widget.attrs["class"] = "form-control custom-select"
    
    class Meta:
        model = UserRole
        fields = ["role",]

