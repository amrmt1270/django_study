from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('next', views.next, name = 'next'),
    path('<int:age>/<name>/<int:id>',views.information, name = 'information'),
    path('form', views.form, name = 'form'),
    path('result', views.form_result, name = 'form_result'),
    path('new_form', views.new_form, name = 'new_form')
]