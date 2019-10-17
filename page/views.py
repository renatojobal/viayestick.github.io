from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.

# View de testeo
def hello_world(request):
    return HttpResponse("Hello world!")

# View principal
def index(request):
    return HttpResponse("Hello my friend, its working!")