from rest_framework.viewsets import ModelViewSet
from .models import Avaliacao
from .serializers import AvaliacaoSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes=[IsAuthenticatedOrReadOnly,]
    filter_backends = [DjangoFilterBackend,SearchFilter ]
    filterset_fields = ['nota']
    search_fields = ['nota']