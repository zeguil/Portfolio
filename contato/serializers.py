from rest_framework.serializers import ModelSerializer
from collections import OrderedDict
from .models import Contato

class ContatoSerializer(ModelSerializer):
    class Meta:
        model = Contato
        fields = ['tipo','numero', 'link']

    def to_representation(self, instance):
        resultado = super(ContatoSerializer, self).to_representation(instance)
        return OrderedDict([(key, resultado[key]) for key in resultado if resultado[key] is not None])