from django import forms
from django.forms import Form 

class TitleTextBlock(Form):
    title = forms.CharField(label="Title", max_length=100)
    text = form.CharField(label="Text", widget=forms.TextArea)