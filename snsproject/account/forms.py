from django.contrib.auth.forms import UserCreationForm
from .models import Account

class AccountSignupForm(UserCreationForm):
    class Meta :
        model = Account
        fields = ('username', 'password1', 'password2')