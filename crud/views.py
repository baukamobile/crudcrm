from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.urls import reverse
from .forms import CreateTaskForm, UpdateTaskForm, RegisterForm, LoginForm
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


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # form.save()
            # return redirect('/home')
            pass
    return render(request, 'registration/login.html', context={'form':form})


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request)
            return redirect('/home')

    else:
        form = RegisterForm()
    
    return render(request, 'registration/sign_up.html', context={'form':form})
