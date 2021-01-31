from django.shortcuts import render
from django.http import *
from . import models


def index(request):
    return render(request, "scrapy_ui.html")

