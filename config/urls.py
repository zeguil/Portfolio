from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from curso.viewsets import CursoViewSet
from avaliacao.viewsets import AvaliacaoViewSet
from contato.viewsets import ContatoViewSet

router = DefaultRouter()

router.register('avaliacao', AvaliacaoViewSet)
router.register('cursos', CursoViewSet)
router.register('contato', ContatoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
