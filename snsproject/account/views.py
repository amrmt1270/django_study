from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AccountSignupForm, AccountLoginForm,PasswordChangeForm,AccountEmailChangeForm, AccountPasswordResetform, AccountSetPasswordForm,AccountAvatorUploadForm
from .models import Account, Follow
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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

class AccountPasswordResetView(auth_views.PasswordResetView):
    subject_template_name = 'account/mail/password_reset_subject.txt'
    email_template_name = 'account/mail/password_reset_message.txt'
    form_class = AccountPasswordResetform
    template_name = 'account/password_reset.html'
    success_url = reverse_lazy('password_reset_done')

class AccountPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

class AccountPasswordResetConfirm(auth_views.PasswordResetConfirmView):
    form_class = AccountSetPasswordForm
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class AccountPasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'

class AccountAvatorUploadView(LoginRequiredMixin, generic.FormView):
    template_name = 'account/avator_upload_form.html'
    form_class = AccountAvatorUploadForm

    def form_valid(self, form):
        user = self.request.user
        avator = form.cleaned_data['avator']
        account = Account.objects.get(username = user)
        account.avator = avator
        account.save()
        return redirect('avator_upload_done')

class AccountAvatorUploadDoneView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'account/avator_upload_done.html'

@login_required
def post_follow(request, pk):
    if request.method == 'POST' :
        follow_user = Account.objects.get(pk = pk)
        if request.user == follow_user:
            messages.error(request, '自分に対してはフォローできません')
            return redirect(to = '/')
        follow_user.follower_count += 1
        follow_user.save()

        request.user.following_count += 1
        request.user.save()

        follow = Follow()
        follow.follow_id = request.user
        follow.follower_id = follow_user
        follow.save()

        messages.success(request, 'ユーザーをフォローしました')
    else:
        messages.error(request, '正しい方法でフォローしてください')
    return redirect(to ='/')