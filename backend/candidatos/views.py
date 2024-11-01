from candidatos.models import DadosPessoais, Contato, Experiencia, FormacaoAcademica, Habilidade, Curriculo, Candidatos
from candidatos.serializers import DadosPessoaisSerializer, ContatoSerializer, ExperienciaSerializer, FormacaoAcademicaSerializer, HabilidadeSerializer, CurriculoSerializer 
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from candidatos.throttles import CurriculoAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class DadosPessoaisViewSet(viewsets.ModelViewSet):
    queryset = DadosPessoais.objects.all().order_by("id")
    serializer_class = DadosPessoaisSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','cpf']
    
class ContatosViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de contato.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = Contato.objects.all().order_by("id")
    serializer_class = ContatoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ExperienciasViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de experiências profissionais.

    Métodos HTTP Permitidos:
    - GET, POST

    Throttle Classes:
    - MatriculaAnonRateThrottle: limite de taxa para usuários anônimos.
    - UserRateThrottle: limite de taxa para usuários autenticados.
    """
    queryset = Experiencia.objects.all().order_by("id")
    serializer_class = ExperienciaSerializer
    http_method_names = ["get", "post"]

class FormacoesAcademicasViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return super().get_queryset().order_by("universidade")
    serializer_class = FormacaoAcademicaSerializer
    
class Habilidades(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Habilidade.order_by("nome")
        return queryset
    serializer_class = HabilidadeSerializer
    
class CurriculosViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de currículos.
    """
    queryset = Curriculo.objects.all()
    serializer_class = CurriculoSerializer  
    