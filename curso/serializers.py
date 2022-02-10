from rest_framework.serializers import ModelSerializer
from collections import OrderedDict
from .models import Curso

class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id','nome','carga_horaria', 'conclusao','link', 'pdf']

    def to_representation(self, instance):
        resultado = super(CursoSerializer, self).to_representation(instance)
        return OrderedDict([(key, resultado[key]) for key in resultado if resultado[key] is not None])