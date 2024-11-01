from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from candidatos.views import (
    DadosPessoaisViewSet,
    ContatosViewSet,
    ExperienciasViewSet,
    FormacoesAcademicasViewSet,
)

router = routers.DefaultRouter()
router.register(r'dadospessoais', DadosPessoaisViewSet)
router.register(r'contatos', ContatosViewSet)
router.register(r'experiencias', ExperienciasViewSet)
router.register(r'formacoes', FormacoesAcademicasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]