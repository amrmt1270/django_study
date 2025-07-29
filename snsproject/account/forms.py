from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import Account
from django.forms.models import ModelForm

class AccountSignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AccountSignupForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta :
        model = Account
        fields = ('username', 'password1', 'password2')


class AccountLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AccountLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta :
        model = Account
        fields = ('username', 'password1',)

class AccontPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Account

class AccountEmailChangeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-controll'
    class Meta:
        model = Account
        fields = ('email', )
    
class AccountPasswordResetform(PasswordResetForm):
    def __init__(self, * args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    
    class Meta :
        model = Account

class AccountSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        for field in self.fields.values() :
            field.widget.attrs['class'] = 'form-control'
    
    class Meta :
        model = Account

class AccountAvatorUploadForm(ModelForm):
    class Meta:
        model = Account
        fields = ('avator', )