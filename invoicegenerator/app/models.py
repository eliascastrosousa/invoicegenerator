from django.db import models

# Create your models here.
from django.db import models

class Company(models.Model):
    username = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    cep = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=20)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=20)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nome