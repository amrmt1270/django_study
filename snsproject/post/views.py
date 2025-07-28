from django.shortcuts import render, redirect
from django.views import generic
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'post/home.html'

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST['content']
        user = request.user
        post = Post()
        post.content = content
        post.owner = user
        post.save()
        messages.success(request, '新しいメッセージを投稿しました。')
        return redirect(to = '/')
    else:
        form = PostForm()
    params = {
        'form' : form
    }
    return render(request, 'post/create.html', params)

def index(request, num = 1):
    data = Post.objects.all()
    page = Paginator(data, 5)
    params = {
        'object_list':data
    }
    return render(request, 'post/home.html', params)