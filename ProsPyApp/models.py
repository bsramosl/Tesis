from django.db import models
from django.contrib.auth.models import User



class TipoReactor(models.Model):
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    especificaciontecnica = models.TextField(max_length=300, blank=False, null=False)
    tiporeactor = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = 'tiporeactor'
        verbose_name_plural = 'tiporeactores'
        ordering = ['tiporeactor']

    def __str__(self):
        return self.descripcion


class Organismo(models.Model):
    nombrecientifico = models.CharField(max_length=50, blank=False, null=False)
    genero = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'organismo'
        verbose_name_plural = 'organismos'
        ordering = ['nombrecientifico']

    def __str__(self):
        return self.nombrecientifico