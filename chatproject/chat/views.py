from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import CreateRoomForm,MessageForm
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

class RoomDetailView(generic.DetailView):
    template_name = 'room/detail.html'
    model = Room

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = self.object.messages.all()
        context['form'] = MessageForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid() :
            message = form.save(commit = False)
            message.room = self.get_object()
            message.posted_by = request.user
            message.seve()
            return redirect('room.detail', pk = self.get_object().pk)
        return self.get(request, *args, **kwargs)

