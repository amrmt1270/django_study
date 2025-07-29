from django.urls import path, include
from . import views
urlpatterns = [
    path('signup/', views.AccountSignUpView.as_view(), name = 'signup'),
    path('login/', views.AccountLoginView.as_view(), name = 'login'),
    path('logout/', views.AccountLogoutView.as_view(), name = 'logout'),
    path('<int:pk>', views.AccountDetailView.as_view(), name = 'detail'),
    path('password_change/', views.AccountPasswordChangeView.as_view(), name = 'password_change'),
    path('password_change/done/', views.AccountPasswordChangeDoneView.as_view(),
        name = 'password_change_done'),
    path('email/change/',views.AccountEmailChangeView.as_view(),name = 'email_change'),
    path('email/change/done/', views.AccountEmailChangeDoneView.as_view(), name = 'email_change_done'),
    path('email/change/complete/<str:token>/', views.AccountEmailChangeCompleteView.as_view(), name = 'email_change_complete'),
]