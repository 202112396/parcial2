from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuarios
from django.db import IntegrityError

# Create your views here.
def inicio(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def create_user(request):
    New_usr = Usuarios(
        user_id=request.POST['user_id'],
        firstName=request.POST['firstName'], 
        lastName=request.POST['lastName'], 
        dpi=request.POST['dpi'], 
        age=request.POST['age'], 
        tel=request.POST['tel'], 
        email=request.POST['email'], 
        password=request.POST['password']
    )
    
    if request.method == 'POST':
        try:
            message = "¡Creaste tu usuario con éxito!"
            New_usr.save()
            return render(request, 'login.html', {'message': message})

        except IntegrityError:
            message = "Este usuario ya existe"
            return render(request, 'register.html', {'message': message})            
    return render(request, 'register.html')

def recover(request):
    return render(request, 'forgot.html')

    #New_usr.save()
    #messages.success(request,'¡Creación exitosa! Ya puedes ingresar')
    #return redirect('/inicio/')