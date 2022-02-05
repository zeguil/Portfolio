from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
import mimetypes
from .models import Curso
from .serializers import CursoSerializer
from django.http import FileResponse





class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(methods=['GET'], detail=True)
    def download(self, request, **kwargs):
        att = self.get_object()
        file_handle = att.pdf.open()

        mimetype, _ = mimetypes.guess_type(att.pdf.path)
        response = FileResponse(file_handle, content_type=mimetype)
        response['Content-Length'] = att.pdf.size
        response['Content-Disposition'] = "attachment; filename={}".format(att.pdfname)
        return response
