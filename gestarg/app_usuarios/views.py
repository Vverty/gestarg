# app_usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirige a la página de inicio de sesión
    else:
        form = UserRegistrationForm()
    return render(request, 'app_usuarios/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'app_usuarios/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'app_usuarios/profile.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')

def registration_complete(request):
    return render(request, 'app_usuarios/registration_complete.html')




