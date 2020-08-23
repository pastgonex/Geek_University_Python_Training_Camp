# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello Django!')


def year(request, year):
    return HttpResponse(year)


def name(request, **kwargs):
    return HttpResponse(kwargs['year'] + kwargs['name'])


def myyear(request,year):
    return render(request, 'yearview.html')

