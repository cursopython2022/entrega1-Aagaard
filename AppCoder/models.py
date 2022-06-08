from django.db import models

# Create your models here.


class argentino(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre+""+str(self.apellido)


class extranjero(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40) 
    dni = models.IntegerField()
    nombre = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.nombre+""+str(self.apellido)

class nacionalizado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre+""+str(self.apellido)


