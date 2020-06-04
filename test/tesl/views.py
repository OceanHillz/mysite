from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm


def index(request):
    return render(request, 'tesl/index.html', {})


def user_logout(request):
    logout(request)
    return redirect('tesl:login')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}')
            return redirect('tesl:home')
        else:
            return redirect('tesl:login')
    else:
        return render(request, 'tesl/login.html', {})


def register_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            messages.success(request, f'Welcome {user.username}')
            return redirect('tesl:home')
    return render(request, 'tesl/register.html', {'form': form})
