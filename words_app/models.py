from django.db import models

# Create your models here.

class Procesamiento(models.Model):
    archivo = models.CharField(max_length=30)
    numero_palabras = models.IntegerField(blank=True, null=True)
    resultado = models.TextField(verbose_name='resultado', null=True)

    def __str__(self):
        return '%s' % self.archivo