

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from familia.models import Familia

def inicio (request):
    datos = {"mensaje": "Bienvenid@ la app de la familia de Sol!"}
    plantilla = loader.get_template("index.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

  
def mama (request):
    datos = {"nombre": "Cristina", "edad": 71, "fecha_nac": "1950-11-06"}
    plantilla = loader.get_template("mama.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

  
def papa (request):
    datos = {"nombre": "Juan", "edad": 70, "fecha_nac": "1951-08-06" }
    plantilla = loader.get_template("papa.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def hermana (request):
    datos = {"nombre": "Lucila", "edad": 40, "fecha_nac": "1982-06-11" }
    plantilla = loader.get_template("hermana.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def base_de_datos(request):
    datos = {"nombres": ["Cristina", "Juan", "Lucila"]}
    plantilla = loader.get_template("basededatos.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)