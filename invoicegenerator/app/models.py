from django.db import models
from usuarios.models import AdditionalData
from django.db.models import F


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
      

class Contador(models.Model):
    nota_fiscal = models.IntegerField(default=1)

    @classmethod
    def gerar_nota_fiscal(cls):
        contador, created = cls.objects.get_or_create(pk=1)
        contador.nota_fiscal += 1
        contador.save()
        return contador.nota_fiscal
    

class Invoice(models.Model):
    username = models.CharField(max_length=100)
    num_invoice = models.IntegerField(default=1)
    nome_emissor = models.CharField(max_length=100)
    sobrenome_emissor = models.CharField(max_length=100)
    email_emissor = models.CharField(max_length=50)
    cnpj_emissor = models.CharField(max_length=100)
    swiftcode = models.CharField(max_length=100) 
    ibancode = models.CharField(max_length=100) 
    salario = models.CharField(max_length=100)

    cep_emissor = models.CharField(max_length=10)
    logradouro_emissor = models.CharField(max_length=100)
    complemento_emissor = models.CharField(max_length=100)
    num_emissor = models.CharField(max_length=5)
    bairro_emissor = models.CharField(max_length=50)
    cidade_emissor = models.CharField(max_length=50)
    estado_emissor = models.CharField(max_length=50)

    nome_destinatario = models.CharField(max_length=100)
    cnpj_destinatario = models.CharField(max_length=100)

    cep_destinatario = models.CharField(max_length=10)
    logradouro_destinatario = models.CharField(max_length=100)
    num_destinatario = models.CharField(max_length=5)
    bairro_destinatario = models.CharField(max_length=50)
    cidade_destinatario = models.CharField(max_length=50)
    estado_destinatario = models.CharField(max_length=50)
    
    issuedate = models.DateField() 
    duedate = models.DateField() 
    

    def __str__(self):
        return self.num_invoice