from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AdditionalData

        

@login_required(login_url="/auth/login/")
def perfil(request):
        return render(request, 'perfil.html')

@login_required(login_url="/auth/login/")
def additionaldata(request):
    additionaldata = AdditionalData.objects.filter(username = request.user.username)
    return render(request, 'additionaldata.html',{'additionaldata': additionaldata})


@login_required(login_url="/auth/login/")
def additionaldata_register(request):
        return render(request, 'additionaldata_register.html')

@login_required(login_url="/auth/login/")
def additionaldata_save(request):
    if request.method == "GET":
        return render(request, 'additionaldata.html')
    else:
        username = request.user.username
        cnpj = request.POST.get('cnpj')
        swiftcode = request.POST.get('swiftcode')
        ibancode = request.POST.get('ibancode')
        salario = request.POST.get('salario')
        cep = request.POST.get('cep')
        logradouro = request.POST.get('logradouro')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        AdditionalData.objects.create(
            username = username,
            cnpj = cnpj,
            swiftcode = swiftcode,
            ibancode = ibancode,
            salario = salario,
            cep = cep,
            logradouro = logradouro,
            numero = numero,
            complemento = complemento,
            bairro = bairro,
            cidade = cidade,
            estado = estado
        )
         
    return redirect(additionaldata)