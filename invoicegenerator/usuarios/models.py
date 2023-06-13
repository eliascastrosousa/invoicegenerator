from django.db import models

class Endereco(models.Model):
    username = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    swiftcode = models.CharField(max_length=100)
    ibancode = models.CharField(max_length=100)
    salario = models.FloatField(max_length=10)
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=10)

    def __str__(self):
        return self.logradouro
