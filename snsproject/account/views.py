from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views
from .forms import AccountSignupForm, AccountLoginForm

from .models import Account

# Create your views here.
class AccountSignUpView(generic.CreateView):
    form_class = AccountSignupForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

class AccountLoginView(auth_views.LoginView):
    form_class = AccountLoginForm
    template_name = 'account/login.html'

class AccountLogoutView(auth_views.LogoutView):
    template_name = 'account/logout.html'

class AccountDetailView(generic.DetailView):
    model = Account
    template_name = 'account/detail.html'