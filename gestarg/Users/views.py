from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from datetime import datetime
from .forms import UserRegisterForm

def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, 'AppFinanzas/index.html')

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "Users/login.html", {"form": form, "msg_login": msg_login})

def index_users(request):
    current_year = datetime.now().year
    return render(request, 'Users/index_users.html', {'current_year': current_year})

def register(request):

    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"Users/index_users.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"Users/register.html" ,  {"form":form, "msg_register": msg_register})

def nosotros(request):
    return render(request, 'Users/nosotros.html')
