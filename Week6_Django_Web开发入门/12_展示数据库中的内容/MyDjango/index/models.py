from django.db import models


# Create your models here.
# 图书 or 电影
class Type(models.Model):
    typename = models.CharField(max_length=20)


class Name(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    stars = models.CharField(max_length=5)