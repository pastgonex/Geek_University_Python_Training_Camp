from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
from .models import Name

def index(request):
    return HttpResponse('Hello Django by 倪彬琪!')


def year(request, year):
    return redirect('/2020.html')


def name(request, **kwargs):
    return HttpResponse(kwargs['name'])


def myyear(request, year):
    return render(request, 'yearview.html')


def books(request):
    # 从models中取数据传给template
    n = Name.objects.all()
    return render(request,'bookslist.html', locals())

