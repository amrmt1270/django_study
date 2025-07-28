from django import forms

class PostForm(forms.Form):
    content = forms.CharField(max_length = 5000)
    wiget = forms.Textarea(attrs = {'class': 'form-controll'})