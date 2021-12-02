from typing import ContextManager

from django.db.models.lookups import IContains
from AppCoder.forms import FormularioUsuarios
from AppCoder.models import Usuarios
from django.db.models import Q
from django.shortcuts import render
from AppCoder import models
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request,'AppCoder/index.html',{})

def crear_usuario(request):
    usuario=None
    if request.method == "POST":
        formulario=FormularioUsuarios(request.POST)
        if formulario.is_valid():
            dato_usuario=formulario.cleaned_data
            usuario=Usuarios(nombre=dato_usuario['nombre'],apellido=dato_usuario['apellido'],dni=dato_usuario['dni'])
            usuario.save()
            formulario=FormularioUsuarios() 
    else:
        formulario=FormularioUsuarios()        
    return render(request,'AppCoder/link1.html', {'usuario':usuario, 'formulario': formulario})

def buscar(request):
    usuario=None
    error=None
    if request.method =='GET':
        dni=request.GET.get('numero', None)
        if dni == '':
            usuarios=Usuarios.objects.all()
        try:
            dni=int(dni)
            usuario=Usuarios.objects.filter(dni=dni)
        except:
            error = 'Ingrese el numero sin puntos o letras'  
    return render(request, 'AppCoder/link2.html', {"usuarios": usuario, "error": error})
                  
def link3(request):
    return render(request,'AppCoder/link3.html',{})

def link4(request):
    return render(request,'AppCoder/link4.html',{})    
    
    





