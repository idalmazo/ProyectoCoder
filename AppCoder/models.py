from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()

class Clientes(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Servicios(models.Model):
    nombre= models.CharField(max_length=30)
    profesional= models.CharField(max_length=30)

class Proveedores(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
