from django import forms
from blog.models import *


def get_category_list():
    data = []
    for cat in Category.objects.all():
        data.append((cat.id, cat.name))
    data = tuple(data)
    return


class CategoryForm(forms.Form):
    category = forms.CharField(label='Category', max_length=100)

    def clean_category(self):
        data = self.cleaned_data['category']
        return data


class TagForm(forms.Form):
    tag = forms.CharField(label='Tag', max_length=100)

    def clean_category(self):
        data = self.cleaned_data['tag']
        return data

class PostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=150)
    subtitle = forms.CharField(label='Subtitle', max_length=250)
    body = forms.CharField(label='Title', widget=forms.Textarea)
    # category = forms.ChoiceField(label='Category', widget=forms.Select, choices=get_category_list())

class UserBasicForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.CharField(label="Email")
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password")

class UserForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.CharField(label="Email", max_length=200)
    mobile = forms.CharField(label="Mobile", max_length=15)
    bio = forms.CharField(label="Bio", max_length=250)
    about = forms.CharField(label="About", widget=forms.Textarea)

class SiteForm(forms.Form):
    site_name = forms.CharField(label="Site Name", max_length=120)

class PermissionForm(forms.Form):
    permission_name = forms.CharField(label="Permission Name", max_length=250)