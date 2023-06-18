from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from .models import Company, AdditionalData, Contador, Invoice
from datetime import datetime, timedelta
from django.utils import timezone


@login_required(login_url="/auth/login/")
def companydetails(request, id):
    company = Company.objects.filter(id=id)
    return render(request, 'companydetails.html', {"company":company})

@login_required(login_url="/auth/login/")
def home(request):
    return render(request, 'home.html')

@login_required(login_url="/auth/login/")
def companylist(request):
    additionalData = AdditionalData.objects.filter(username = request.user.username)
    company = Company.objects.filter(username = request.user.username)
    return render(request, 'companylist.html',{'company': company, "additionalData":additionalData})

@login_required(login_url="/auth/login/")
def companyregister(request):
    return render(request, 'companyregister.html')

@login_required(login_url="/auth/login/")
def invoicecreate(request):
    return render(request, 'invoicecreate.html')

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

def calcular_datas():
    data_atual = timezone.now().date()
    data_emissao = data_atual
    data_vencimento = data_emissao + timedelta(days=7)
    return data_emissao, data_vencimento


@login_required(login_url="/auth/login/")
def invoicecreate(request, id):
    company = Company.objects.get(id=id)
    usuarios = User.objects.filter(username = request.user.username)
    dadoscomplementares = AdditionalData.objects.filter(username = request.user.username)
    

    return render(request, 'invoicecreate.html',{"company":company,"dadoscomplementares":dadoscomplementares, "usuarios":usuarios})

@login_required(login_url="/auth/login/")
def invoice_save(request):
    if request.method == "GET":
        return render(request, 'invoicecreate.html')
    else:
        username = request.user.username
        nota_fiscal = Contador.gerar_nota_fiscal()
        nota_fiscal = str(nota_fiscal).zfill(4)
        nome_emissor = request.POST.get('nome_emissor')
        sobrenome_emissor = request.POST.get('sobrenome_emissor')
        email_emissor = request.POST.get('email_emissor')
        cnpj_emissor = request.POST.get('email_emissor')
        swiftcode = request.POST.get('swiftcode')
        ibancode = request.POST.get('ibancode')
        salario = request.POST.get('salario')

        cep_emissor = request.POST.get('cep_emissor')
        logradouro_emissor = request.POST.get('logradouro_emissor')
        num_emissor = request.POST.get('num_emissor')
        complemento_emissor = request.POST.get('complemento_emissor')
        bairro_emissor = request.POST.get('bairro_emissor')
        cidade_emissor = request.POST.get('cidade_emissor')
        estado_emissor = request.POST.get('estado_emissor')

        nome_destinatario = request.POST.get('nome_destinatario')
        cnpj_destinatario = request.POST.get('cnpj_destinatario')
        logradouro_destinatario = request.POST.get('logradouro_destinatario')
        bairro_destinatario = request.POST.get('bairro_destinatario')
        cidade_destinatario = request.POST.get('cidade_destinatario')

        issuedate = request.POST.get('issuedate')
        duedate = request.POST.get('duedate')


        
        Invoice.objects.create(
            username = username,
            num_invoice = nota_fiscal,
            nome_emissor = nome_emissor,
            sobrenome_emissor = sobrenome_emissor,
            email_emissor = email_emissor,
            cnpj_emissor = cnpj_emissor,
            swiftcode = swiftcode,
            ibancode = ibancode,
            salario = salario,

            cep_emissor = cep_emissor,
            logradouro_emissor = logradouro_emissor,
            num_emissor = num_emissor,
            complemento_emissor = complemento_emissor,
            bairro_emissor = bairro_emissor,
            cidade_emissor = cidade_emissor,
            estado_emissor = estado_emissor,

            nome_destinatario = nome_destinatario,
            cnpj_destinatario = cnpj_destinatario,
            logradouro_destinatario = logradouro_destinatario,
            bairro_destinatario = bairro_destinatario,
            cidade_destinatario = cidade_destinatario,
            
            issuedate = issuedate,
            duedate = duedate
        )
    return redirect(companylist)

@login_required(login_url="/auth/login/")
def invoicelist(request):
    notafiscal = Invoice.objects.filter(username = request.user.username)
    return render(request, 'invoicelist.html', {"notafiscal":notafiscal})

@login_required(login_url="/auth/login/")
def invoicedetails(request, id):
    notafiscal = Invoice.objects.filter(id=id)
    return render(request, 'invoicedetails.html', {"notafiscal":notafiscal})

@login_required(login_url="/auth/login/")
def invoicesearch(request):
    txt_search = request.GET.get('search')
    if txt_search:
        if Invoice.objects.filter(num_invoice__icontains = txt_search):
            notafiscal = Invoice.objects.filter(num_invoice__icontains = txt_search)
            return render(request, 'invoicelist.html', {"notafiscal":notafiscal} )
    else:
        notafiscal = Invoice.objects.all()
        return render(request, 'invoicelist.html', {"notafiscal":notafiscal} )