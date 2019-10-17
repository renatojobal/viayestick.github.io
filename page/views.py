from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

# View de testeo
def hello_world(request):
    return HttpResponse("Hello world!")

# View principal
def index(request):
    return render(request, 'page/index.html')