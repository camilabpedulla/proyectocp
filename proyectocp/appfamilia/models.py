from pyexpat import model
from django.db import models
from datetime import datetime

class familia (models.Model):
    nombre= models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_de_nacimiento= models.DateField(default= datetime.now())
