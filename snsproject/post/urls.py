from collections import namedtuple
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:num>', views.index, name = 'index'),
    path('post/create/', views.create_post, name = 'create'),
    path('post/<int:pk>', views.post_detail, name = 'detail'),
    path('post/<int:pk>/delete', views.post_delete, name = 'delete'),
    path('post/<int:pk>/favorite', views.post_favorite, name = 'favorite')
]