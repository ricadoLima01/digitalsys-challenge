from django.db import models
from django.core.validators import RegexValidator

telefone = models.CharField(
    max_length=11,
    validators=[RegexValidator(regex=r'^\d{10,11}$', message='Insira um número de telefone válido.')]
)


class DadosPessoais(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False, max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    celular = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\d{2} \d{5}-\d{4}$', message='Insira um número de celular válido.')])
    
    def __str__(self):
        return self.nome
    

class Contato(models.Model):
    telefone = models.CharField(max_length=11)
    logradouro = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    
    def __str__(self):
        return self.telefone

class Experiencia(models.Model):
    empresa = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    inicio_data = models.DateField()
    fim_data = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.empresa

class FormacaoAcademica(models.Model):
    universidade = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    inicio_data = models.DateField()
    fim_data = models.DateField()
    
    def __str__(self):
        return self.universidade

class Habilidade(models.Model):
    nome = models.CharField(max_length=100)
    estudante_nome = models.ForeignKey(DadosPessoais, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.estudante_nome.nome   

class Curriculo(models.Model):
    dados_pessoais = models.OneToOneField(DadosPessoais, on_delete=models.CASCADE)
    contato = models.OneToOneField(Contato, on_delete=models.CASCADE)
    experiencia = models.ManyToManyField(Experiencia)
    formacao_academica = models.ManyToManyField(FormacaoAcademica)
    habilidades = models.ManyToManyField(Habilidade)
        
    def __str__(self):
        return self.dados_pessoais.nome

class Candidatos(models.Model):
    dados_pessoais = models.OneToOneField('DadosPessoais', on_delete=models.CASCADE, related_name='candidato')
    contato = models.OneToOneField('Contato', on_delete=models.CASCADE, related_name='candidato')
    experiencias = models.ManyToManyField('Experiencia', related_name='candidatos')
    formacoes_academicas = models.ManyToManyField('FormacaoAcademica', related_name='candidatos')
    habilidades = models.ManyToManyField('Habilidade', related_name='candidatos')
    
    def __str__(self):
        return self.dados_pessoais.nome
    