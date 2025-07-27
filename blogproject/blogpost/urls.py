from django.contrib import admin
from django.urls import path
from .views import BlogList

urlpatterns = [
    path('list/', BlogList.as_view()),
]