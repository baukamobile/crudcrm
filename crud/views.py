from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.urls import reverse
from .forms import CreateTaskForm
# Create your views here.


def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', context={'tasks':tasks})

def create_task(request):
    form = CreateTaskForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            create_task_form=form.save()
            # return redirect('home')
        return redirect(reverse('home'))
    return render(request,'create_task.html', context={'form':form, })

def update_task(request):
    pass

def delete_task(request):
    pass