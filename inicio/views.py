from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuarios

# Create your views here.
def inicio(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def create_user(request):
    New_usr = Usuarios(
        user_id=request.POST['user_id'], 
        )
    New_usr.save()
    messages.success(request,'¡Creación exitosa! Ya puedes ingresar')
    return redirect('/inicio/')