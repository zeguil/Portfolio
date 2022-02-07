from .models import Contato
from .serializers import ContatoSerializer
from rest_framework.viewsets import ModelViewSet

class ContatoViewSet(ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer