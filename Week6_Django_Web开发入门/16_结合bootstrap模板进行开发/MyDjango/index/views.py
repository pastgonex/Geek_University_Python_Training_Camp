from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Name


def index(request):
    return HttpResponse('Hello Django!  By 倪彬琪!')


def year(request, year):
    return redirect('/2020.html')


def name(request, **kwargs):
    return HttpResponse(kwargs['name'])


def myyear(request, year):
    return render(request, 'yearview.html')


def books(request):
    n = Name.objects.all()
    return render(request, 'bookslist.html', locals())
