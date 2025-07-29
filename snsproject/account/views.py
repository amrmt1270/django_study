from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AccountSignupForm, AccountLoginForm,PasswordChangeForm,AccountEmailChangeForm
from .models import Account
from django.core.signing import BadSignature, SignatureExpired, dumps, loads
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

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

class AccountPasswordChangeView(LoginRequiredMixin, auth_views.PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'account/password_change.html'


class AccountPasswordChangeDoneView(LoginRequiredMixin, auth_views.PasswordResetDoneView):
    template_name = 'account/password_change_done.html'


class AccountEmailChangeView(LoginRequiredMixin, generic.FormView):
    template_name = 'account/email_change_form.html'
    form_class = AccountEmailChangeForm

    def form_valid(self, form):
        user = self.request.user
        new_email = form.cleaned_data['email']

        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protcol':'https' if self.request.is_secure() else 'http',
            domain : 'domain',
            'token' : dumps(new_email),
            'user' : user
        }
        subject = render_to_string('account/mail/email_change_subject.txt', context)
        message = render_to_string('account/mail/email_change_message.txt', context)

        send_mail(subject, message, None, [new_email])
        return redirect('email_chnage_done')

class AccountEmailChangeDoneView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'account/email_change_done.html'

class AccountEmailChangeCompleteView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, **kwargs):
        token = kwargs.get('token')
        try :
            new_email = loads(token, max_age=60*60*24)
        except SignatureExpired:
            return HttpResponseBadRequest()
        except BadSignature:
            return HttpResponseBadRequest()
        else:
            request.user.email = new_email
            request.user.save()
            return super().get(request, **kwargs)