from django.contrib.messages.api import warning
from django.shortcuts import redirect, render
#Formularios de Django
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
#Login
from django.contrib.auth import authenticate,login,logout
#Mensajes Flash
from django.contrib import messages
#Decoradores de autenticación(se ejecutan antes de la función)
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request) :
    return render(request, 'mainapp/index.html', {
        'title':'Inicio'
    })
def about(request) :
    return render(request, 'mainapp/about.html', {
        'title':'Sobre Nosotros'
    } ) 

def register_page(request) :

    register_form = RegisterForm()

    if request.method == 'POST' :
       register_form = RegisterForm(request.POST)
       if register_form.is_valid():
           register_form.save()
           #mensaje flash
           messages.success(request,'Te has registrado correctamente')
           return redirect('sobrenosotros')

    return render(request ,'users/register.html', {
        'title' : 'Registro',
        'register_form': register_form
    }) 

def login_user(request) :
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =  authenticate(request,username=username, password=password)

        if user is not None :
            login(request,user)
            return redirect('sobrenosotros')
        else:
            messages.warning(request,'No te has podido identificar')    


    return render(request,'users/login.html', {
        'title' : 'Login'
    }) 

#login_required va a restringir la ruta /logout requiriendo que esté logueado
#y redirecciona a login
@login_required(login_url="login")
def logout_user(request) :
    logout(request)
    return redirect('sobrenosotros')    
