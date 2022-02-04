from django.shortcuts import render
from .models import Curso

def download(request, pk):
    obj = Curso.objects.get(pk=pk)
    resp = obj.pdf
    return Response(resp)
