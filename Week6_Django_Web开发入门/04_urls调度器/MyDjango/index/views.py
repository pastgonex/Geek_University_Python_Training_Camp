# index/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# 自定义的
def index(request):
    return HttpResponse("Hello Django!")

