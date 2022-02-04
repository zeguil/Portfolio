from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.TimeField()
    conclusao = models.DateField()
    link = models.URLField(unique=True)
    pdf = models.FileField(upload_to='certificado/')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nome

    


