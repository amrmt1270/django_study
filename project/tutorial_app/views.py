from django.shortcuts import render
from django.http import HttpResponse
from .forms import TutorialForm
# Create your views here.

def index(request) :
    if 'msg' and 'title' in request.GET:
        title, msg = request.GET['title'], request.GET['msg']
        params = {
            'title' :title,
            'msg' : msg
            }
    else:
        params = {
            'title':'hello',
            'msg': 'これはサンプルで作ったhello のページです。'
        }
        params['goto'] = 'next'
        params['information'] = 'information'
        params['numbers'] = range(5)
        params['items'] = ['apple', 'tomato', 'banana', 'melon']
    return render(request, 'hello/index.html', params)

def information(request,name,age,id):  
    params={
        'name':name,
        'age':age
    }
    return render(request, 'hello/information.html', params)

def next(request):
    params = {
        'title': 'hello/next',
        'msg' : 'これはサンプルで作ったhello のページです。',
        'goto': 'index'
    }
    return render(request, 'hello/index.html', params)

def form(request):
    params = {
        'title':'Form',
        'msg' : 'メッセージを入力してください。',
    }
    return render(request, 'hello/form.html', params)

def form_result(request):
    msg = request.POST['msg']
    params = {
        'title': 'Form',
        'msg' : msg,
        }
    return render(request, 'hello/form.html', params)

def new_form(request):
    params = {
        'title':'BMI計算機',
        'form' : TutorialForm()
        }
    if (request.method == 'POST'):
        h,w = float(request.POST['height']), float(request.POST['weight'])
        bmi = w /(h/100)**2
        params['bmi'] = bmi
        params['form'] = TutorialForm(request.POST)
    return render(request, 'hello/new_form.html',params)