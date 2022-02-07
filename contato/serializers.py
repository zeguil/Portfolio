
from rest_framework.serializers import ModelSerializer
from .models import Contato

class ContatoSerializer(ModelSerializer):
    class Meta:
        model = Contato
        fields = ['tipo','numero', 'link']