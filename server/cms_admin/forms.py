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
        