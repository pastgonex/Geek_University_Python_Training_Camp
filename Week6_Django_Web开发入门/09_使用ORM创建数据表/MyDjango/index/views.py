# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return HttpResponse('Hello Django! By 倪彬琪')


def year(request, year):
    return redirect('/2020.html')


def name(request, **kwargs):
    return HttpResponse(kwargs['name'])


def myyear(request, year):
    return render(request, 'yearview.html')  # 返回渲染好的 html文本
