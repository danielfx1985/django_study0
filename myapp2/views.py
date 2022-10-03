from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
def index(request):
    return HttpResponse("HELLO! This is myapp2")