from django import forms

class PostForm(forms.Form):
    content = forms.CharField(max_length = 5000, 
                            widget = forms.Textarea(attrs = {'class': 'form-controll'}))
    image = forms.ImageField(label = '画像', required=False)
    VISIBILITY_CHOICE = [
        ('PUBLIC', '公開'),
        ('PRIVATE', '非公開')
    ]
    visibility = forms.fields.ChoiceField(
        choices = VISIBILITY_CHOICE, required = True
    )

