from django.shortcuts import render
from django.http import *
from . import models


def index(request):
    data = models.Schools.objects.all()
    return render(request, "scrapy_ui.html",{"data":data})

