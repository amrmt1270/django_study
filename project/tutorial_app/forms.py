from django import forms

class TutorialForm(forms.Form):
    height = forms.FloatField(label= '身長(cm)')
    weight = forms.FloatField(label = '体重(kg)')