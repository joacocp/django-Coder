# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar




def saludo(request):
   return HttpResponse("Hola Mundo - este es un saludo nuevo")

def saludo_con_render (request):
   return render(request, 'app_principal/saludo.html')

def crear_familiar(request,nombre):
   if nombre is not None:
      
      nuevo_familiar = Familiar(
       nombre = nombre,
       apellido = 'Canedo Pero',
       edad = 30,
       fecha_de_nacimiento = '1994-01-01',
      )
      nuevo_familiar.save()
   return render(request,'app_principal/crear_familiar.html',{'nombre' : nombre})
