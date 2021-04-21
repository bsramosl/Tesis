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


class Reactor(models.Model):
    marca = models.CharField(max_length=50, blank=False, null=False)
    modelo = models.CharField(max_length=50, blank=False, null=False)
    especificaciontecnica = models.TextField(max_length=200, blank=False, null=False)
    foto1 = models.ImageField(upload_to='static/img/')
    foto2 = models.ImageField(upload_to='static/img/')
    foto3 = models.ImageField(upload_to='static/img/')
    foto4 = models.ImageField(upload_to='static/img/')
    estado = models.BooleanField(default=True)
    tiporeactor = models.ForeignKey(TipoReactor,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'reactor'
        verbose_name_plural = 'reatores'
        ordering = ['marca']

    def __str__(self):
        return self.marca


class CaBatch(models.Model):
    titulo = models.CharField(max_length=20, blank=False, null=False)
    descripcion = models.TextField(max_length=200, blank=False, null=False)
    y = models.FloatField(max_length=10, blank=False, null=False)
    ks = models.FloatField(max_length=10, blank=False, null=False)
    umax = models.FloatField(max_length=10, blank=False, null=False)
    ms = models.FloatField(max_length=10, blank=False, null=False)
    f = models.FloatField(max_length=10, blank=False, null=False)
    t = models.FloatField(max_length=10, blank=False, null=False)
    v0 = models.FloatField(max_length=10, blank=False, null=False)
    v = models.FloatField(max_length=10, blank=False, null=False)
    vf = models.FloatField(max_length=10, blank=False, null=False)
    so = models.FloatField(max_length=10, blank=False, null=False)
    n = models.FloatField(max_length=10, blank=False, null=False)
    x = models.FloatField(max_length=10, blank=False, null=False)
    reactor = models.ForeignKey(Reactor,on_delete=models.CASCADE)
    organismo = models.ForeignKey(Organismo,on_delete=models.CASCADE)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'cabatch'
        verbose_name_plural = 'cabatchs'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
