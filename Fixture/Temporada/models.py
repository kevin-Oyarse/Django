from operator import mod
from django.db import models

# Create your models here.

class Equipos(models.Model):
    nombre=models.CharField(max_length=15)

class Resultados (models.Model):
    victorias=models.IntegerField()
    derrotas=models.IntegerField()
    empates=models.IntegerField()
    GC=models.IntegerField()
    GF=models.IntegerField()

class Partidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    terminados=models.BooleanField()