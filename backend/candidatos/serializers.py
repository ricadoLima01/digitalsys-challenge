from rest_framework import serializers
from candidatos.models import DadosPessoais, Contato, Experiencia, FormacaoAcademica, Habilidade, Curriculo
from candidatos.validators import cpf_invalido, nome_invalido, celular_invalido


class DadosPessoaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosPessoais
        fields = ['id','nome','email','cpf','data_nascimento']

    def validate(self,dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter um valor válido'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras'})
        return dados
    

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'
        
    def validate(self,dados):
        if celular_invalido(dados['telefone']):
            raise serializers.ValidationError({'celular':'O celular precisa seguir o modelo: 86 99999-9999 (respeitando traços e espaços)'})
        return dados

class ExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiencia
        exclude = []

class FormacaoAcademicaSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = FormacaoAcademica
        fields = ['id', 'curso', 'periodo']  # Adicionar 'id' aos campos
    def get_periodo(self,obj):
        return obj.get_periodo_display()

class HabilidadeSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta:
        model = Habilidade
        fields = ['estudante_nome']
        
class CurriculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculo
        fields = '__all__'