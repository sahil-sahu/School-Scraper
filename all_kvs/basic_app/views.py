from django.shortcuts import render
from uuid import uuid4
from django.http import *
from . import models
from django.contrib import messages
from django.db.models import Q
from scrapyd_api import ScrapydAPI


def index(request):
    return render(request, "scrapy_ui.html")

