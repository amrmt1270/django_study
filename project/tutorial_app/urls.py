from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('next', views.next, name = 'next'),
    path('<int:age>/<name>/<int:id>',views.information, name = 'information')
]