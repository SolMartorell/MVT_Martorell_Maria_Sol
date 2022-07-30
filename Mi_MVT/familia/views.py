

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context # loader
from datetime import datetime
from familia.models import Familia

def inicio (request):
    datos = {"mensaje": "Bienvenida Sol a la app de tu familia!"}
    archivo  = open(r"C:\Users\msolm\OneDrive\Documents\Curso_Python\VSC\Mi_MVT\Mi_MVT\familia\templates\index.html", "r")
    contenido = archivo.read()
    archivo.close()

    plantilla = Template(contenido)

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)
  
def mama (request):
    datos = {"nombre": "Cristina", "edad": 72, "fecha_nac": "1950-11-06"}
    archivo  = open(r"C:\Users\msolm\OneDrive\Documents\Curso_Python\VSC\Mi_MVT\Mi_MVT\familia\templates\mama.html", "r")
    contenido = archivo.read()
    archivo.close()

    plantilla = Template(contenido)

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)
  
def papa (request):
    datos = {"nombre": "Juan", "edad": 71, "fecha_nac": "1951-08-06" }
    archivo  = open(r"C:\Users\msolm\OneDrive\Documents\Curso_Python\VSC\Mi_MVT\Mi_MVT\familia\templates\papa.html", "r")
    contenido = archivo.read()
    archivo.close()

    plantilla = Template(contenido)

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def hermana (request):
    datos = {"nombre": "Lucila", "edad": 40, "fecha_nac": "1982-06-11" }
    archivo  = open(r"C:\Users\msolm\OneDrive\Documents\Curso_Python\VSC\Mi_MVT\Mi_MVT\familia\templates\hermana.html", "r")
    contenido = archivo.read()
    archivo.close()

    plantilla = Template(contenido)

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

