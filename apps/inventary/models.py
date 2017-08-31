from django.db import models

# Create your models here.


class Lugar(models.Model):

    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = "Lugares"

    def __str__(self):
        return self.nombre
    

class Oficina(models.Model):

    nombre = models.CharField(max_length=200)
    lugar = models.ForeignKey(Lugar)

    class Meta:
        verbose_name = "Oficina"
        verbose_name_plural = "Oficinas"

    def __str__(self):
        return self.nombre

class Estado(models.Model):

    nombre = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return self.nombre
    
    

class Computer(models.Model):

    oficina = models.ForeignKey(Oficina)
    nom_usuario=models.CharField(max_length=50)
    sis_operativo=models.CharField(max_length=100)
    cap_disco = models.IntegerField()
    memoria = models.IntegerField()
    procesador = models.CharField(max_length=100)
    monitor = models.CharField(max_length=100)
    perifericos = models.TextField(max_length=200)
    estado = models.ForeignKey(Estado)
    

    class Meta:
        verbose_name = "Computer"
        verbose_name_plural = "Computers"

    def __str__(self):
        return self.monitor
