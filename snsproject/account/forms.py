from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account

class AccountSignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AccountSignupForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-controll'
    class Meta :
        model = Account
        fields = ('username', 'password1', 'password2')


class AccountLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AccountLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-controll'
    class Meta :
        model = Account
        fields = ('username', 'password1',)