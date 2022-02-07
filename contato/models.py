from django.db import models

class Contato(models.Model):
    tipo = models.CharField(max_length=50)
    numero = models.CharField(max_length=15)
    link = models.URLField()
