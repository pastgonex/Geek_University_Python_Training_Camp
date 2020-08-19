# index/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index) # 匹配空目录, 然后找到 index/views.py 下的 index
]
