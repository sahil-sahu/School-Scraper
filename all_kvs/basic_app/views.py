from django.shortcuts import render
from django.http import *
from . import models


def index(request):
    # data = models.Schools.objects.all()
    return render(request, "index.html")

