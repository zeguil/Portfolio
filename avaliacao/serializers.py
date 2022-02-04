from rest_framework.serializers import ModelSerializer
from .models import Avaliacao

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario']