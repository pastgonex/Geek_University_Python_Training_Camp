from django.urls import re_path, path, register_converter

from . import views,  converters

register_converter(converters.IntConverter, 'myint')
register_converter(converters.FourDigitYearConverter,'yyyy')

urlpatterns = [
    path('', views.index),
    # path('<int:year>', view.year),

    path('<int:year>/<str:name>',views.name),

    # 正则
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),

    # 自定义过滤器
    path('<yyyy:year>', views.year)
]