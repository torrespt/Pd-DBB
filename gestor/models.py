from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    telefono=models.CharField(max_length=10)

class articulo(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField(max_length=10)

class pedido(models.Model):
    numero=models.IntegerField(max_length=10)
    fecha=models.DateField()
    entregado=models.BooleanField()