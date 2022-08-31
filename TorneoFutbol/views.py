from urllib import request
from django.template import Template,Context
from django.http import HttpResponse
from django.template import loader
import random
from django.shortcuts import render

lista_equipos=["Barcelona","Real Madrid","Boca","Villareal","Valencia","Milan","Sevilla","Manchester City"]

def ventana(request):
    lista_equipos=["Barcelona","Real Madrid","Boca","Villareal","Valencia","Milan","Sevilla","Manchester City"]


    return render(request,"myPlantilla.html",{"equipos":lista_equipos})

def Equipos (request):
    return render(request,"equipo.html")

def tabla(request):
    return render(request,"tabla.html")


