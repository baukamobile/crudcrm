from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.urls import reverse
from .forms import CreateTaskForm, UpdateTaskForm
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

def update_task(request, pk):
    current_task = Task.objects.get(id=pk)
    form = UpdateTaskForm(request.POST or None, instance=current_task)
    if form.is_valid():
        form.save()
        return redirect(reverse('home'))
    return render(request, 'update_task.html', context={'form':form,'current_task':current_task})



def delete_task(request, pk):
    delete_tsk = Task.objects.get(id=pk)
    delete_tsk.delete()
    return redirect('home')


def login(request):
    return render(request, 'registration/login.html')