from django.shortcuts import redirect, render
#Formularios de Django
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

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
           return redirect('sobrenosotros')

    return render(request ,'users/register.html', {
        'title' : 'Registro',
        'register_form': register_form
    })       