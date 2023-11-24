from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    password= models.CharField(max_length=30)
    docente = models.BooleanField(default=False)