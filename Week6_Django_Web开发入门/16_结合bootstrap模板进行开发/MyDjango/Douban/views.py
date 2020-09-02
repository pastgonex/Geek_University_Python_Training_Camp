from django.shortcuts import render

# Create your views here.
from .models import T1
from django.db.models import Avg


def books_short(request):
    #  从models取数据传给template
    shorts = T1.objects.all()
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg = f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "  # 从字典中取值
    # print(f"{T1.objects.aggregate(Avg('n_star'))}")
    # print(f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} ")

    # 情感倾向
    sent_avg = f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "  # 用到f是因为要在后面设置精度

    # 正向数量
    queryset = T1.objects.values('sentiment')
    conditions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**conditions).count()

    # 负向数量
    queryset = T1.objects.values('sentiment')
    conditions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**conditions).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())
