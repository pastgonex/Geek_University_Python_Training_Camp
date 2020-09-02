from django.urls import path,include,re_path,register_converter

from . import views

urlpatterns =[
    path('', views.index),
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name = 'urlyear'),

    path('<int:year>', views.year),
    path('<int:year>/<str:name>', views.name),

    path('books', views.books)

]