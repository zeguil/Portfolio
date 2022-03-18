from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    conclusao = models.DateField()
    link = models.URLField(blank=True,null=True, unique=True)
    pdf = models.FileField()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nome

    @property
    def nomepdf(self):
        return self.pdf.name.split('/')[-1:][0]

    


