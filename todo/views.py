from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
from .forms import *
from .decorators import *


@login_required
def home(request):
    tasks = request.user.task_set.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        title = request.POST.get('title')
        if title == '':
            messages.warning(request, 'Field cannot be empty!')
            return redirect('home')
        elif request.user.task_set.filter(title=title).exists():
            messages.warning(request, f'{title} is already exists!')
            return redirect('home')
        else:
            if form.is_valid():
                form.save()
                return redirect('home')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/home.html', context)


@unauthenticated_user
def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        title = request.POST.get('title')
        if title == '':
            messages.warning(request, 'Field cannot be empty!')
            return redirect('home')
        elif request.user.task_set.filter(title=title).exists():
            messages.warning(request, f'{title} is already exists!')
            return redirect('home')
        else:
            if form.is_valid():
                form.save()
                return redirect('home')
    return render(request, 'registration/register.html', {'form': form})


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required
def update(request, pk):
    tasks = Task.objects.get(id=pk)
    form = TaskForm(instance=tasks)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        title = request.POST.get('title')
        if title == '':
            messages.warning(request, 'Field cannot be empty!')
            return redirect('update')
        elif request.user.task_set.filter(title=title).exists():
            messages.warning(request, f'{title} is already exists!')
            return redirect('update', tasks.id)
        else:
            if form.is_valid():
                form.save()
                return redirect('home')
    context = {'form': form}
    return render(request, 'todo/update.html', context)


@login_required
def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('home')
