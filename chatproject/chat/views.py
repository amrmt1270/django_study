from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import CreateRoomForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Room

# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'home.html'

class CreateRoomView(LoginRequiredMixin, generic.CreateView):
    template_name = 'room/create.html'
    form_class = CreateRoomForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

class RoomListView(generic.ListView):
    template_name = 'room/list.html'
    model = Room