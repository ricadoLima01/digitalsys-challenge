from django.db import models

# Create your models here.
class Candidato(models.Model):
    nome = models.CharField(max_length=250)
    data_nascimento = models.DateField()

class Contato(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=250)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=250)
    cidade = models.CharField(max_length=250)
    estado = models.CharField(max_length=250)
    cep = models.CharField(max_length=10)

class Experiencia(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=250)
    cargo = models.CharField(max_length=250)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.TextField()

class Formacao(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    curso = models.CharField(max_length=250)
    instituicao = models.CharField(max_length=250)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.TextField()
    