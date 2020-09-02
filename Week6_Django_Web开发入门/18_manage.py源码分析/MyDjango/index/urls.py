from django.urls import re_path, path, register_converter

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:year>', views.year),
    path('<int:year>/<str:name>', views.name),
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),
    path('books', views.books)
]