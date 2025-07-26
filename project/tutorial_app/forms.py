from django import forms

class TutorialForm(forms.Form):
    name = forms.CharField(label= 'name')
    age = forms.IntegerField(label = 'age')
    message = forms.CharField(label = 'msg')
    