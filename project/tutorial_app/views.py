from django.shortcuts import render
from django.http import HttpResponse
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