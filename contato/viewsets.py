from .models import Contato
from .serializers import ContatoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend



class ContatoViewSet(ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter ]
    permission_classes=[IsAuthenticatedOrReadOnly,]
    filterset_fields = ['tipo']
    search_fields = ['tipo']