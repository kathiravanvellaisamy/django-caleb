from django.shortcuts import render
from django.http import HttpResponse


def movies(request):
    return HttpResponse("<h1>Hello Kathiravan Karthikeyan</h1>") 


def home(request):
    return HttpResponse("<h1>Home Page</h1>")