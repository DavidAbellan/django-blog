#Personalizando un formulario que ya viene por defecto 
#en la librería de Python modificando los models del propio Python

from django import forms
from django.core import validators


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class RegisterForm(UserCreationForm) :
    class Meta :
        model = User
    #fields que están en la bbdd    
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
