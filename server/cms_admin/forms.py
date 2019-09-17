from django import forms  

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


class UserForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.CharField(label="Email", max_length=200)
    mobile = forms.CharField(label="Mobile", max_length=15)
    bio = forms.CharField(label="Bio", max_length=250)
    about = forms.CharField(label="About", widget=forms.Textarea)

class SiteForm(forms.Form):
    site_name = forms.CharField(label="Site Name", max_length=120)