from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
import mimetypes
from .models import Curso
from .serializers import CursoSerializer
from django.http import FileResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly





class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes=[IsAuthenticatedOrReadOnly,]
    filter_backends = [DjangoFilterBackend,SearchFilter ]
    filterset_fields = ['nome']
    search_fields = ['nome']
    
    def query_set(self, request):
        pass

    @action(methods=['GET'], detail=True)
    def download(self, request, **kwargs):
        objeto = self.get_object()
        identificador = objeto.pdf.open()
        mimetype, _ = mimetypes.guess_type(objeto.pdf.path)
        response = FileResponse(identificador, content_type=mimetype)
        response['Content-Length'] = objeto.pdf.size
        response['Content-Disposition'] = f"attachment; filename={objeto.nomepdf}"
        return response
