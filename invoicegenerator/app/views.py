from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from .models import Company

@login_required(login_url="/auth/login/")
def home(request):
    return render(request, 'home.html')

@login_required(login_url="/auth/login/")
def companylist(request):
    company = Company.objects.filter(username = request.user.username)
    return render(request, 'companylist.html',{'company': company})

@login_required(login_url="/auth/login/")
def companyregister(request):
    return render(request, 'companyregister.html')

@login_required(login_url="/auth/login/")
def company_save(request):
    if request.method == "GET":
        return render(request, 'companyregister.html')
    else:
        username = request.user.username
        cnpj = request.POST.get('cnpj')
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        cep = request.POST.get('cep')
        logradouro = request.POST.get('logradouro')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        pais = request.POST.get('pais')

        Company.objects.create(
            username = username,
            cnpj = cnpj,
            nome = nome,
            telefone = telefone,
            email = email,
            cep = cep,
            logradouro = logradouro,
            numero = numero,
            complemento = complemento,
            bairro = bairro,
            cidade = cidade,
            estado = estado,
            pais = pais
        )
         
    return redirect(companylist)


