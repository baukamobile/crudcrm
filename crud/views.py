from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.


def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', context={'task':tasks})

def create_task(request):
    tasks = Task.objects.all()
    return render(request, '')

def update_task(request):
    pass

def delete_task(request):
    pass