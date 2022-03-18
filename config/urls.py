from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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

schema_view = get_schema_view(
   openapi.Info(
      title="API Docs",
      default_version='v1',
      description="Portfolio José Guilherme Lins",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
