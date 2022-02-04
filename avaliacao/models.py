from django.db import models
from curso.models import Curso

class Avaliacao(models.Model):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=2, decimal_places=1)
    comentario = models.TextField()

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return f'{self.curso}'


