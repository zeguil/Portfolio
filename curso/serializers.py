from rest_framework.serializers import ModelSerializer
from .models import Curso

class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id','nome','carga_horaria', 'conclusao','link', 'pdf']