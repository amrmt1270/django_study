from collections import namedtuple
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:num>', views.index, name = 'index'),
    path('post/create/', views.create_post, name = 'create')
]