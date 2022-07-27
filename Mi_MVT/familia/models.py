from django.shortcuts import render
from django.db import models



class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nac = models.DateField()
