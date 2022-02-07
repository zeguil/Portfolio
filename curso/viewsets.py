from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
import mimetypes
from .models import Curso
from .serializers import CursoSerializer
from django.http import FileResponse





class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

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
