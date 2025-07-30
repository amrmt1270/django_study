from django.urls import path, include
from . import views
urlpatterns =[
    path('home/',views.HomeView.as_view(), name = 'home'),
    path('room/create/', views.CreateRoomView.as_view(), name = 'room.create'),
    path('room/list/', views.RoomListView.as_view(), name = 'room.list')
]