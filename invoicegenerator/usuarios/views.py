from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Endereco


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return redirect('companylist')
        else:
            return render(request, 'login.html', {'error': 'Username ou senha invalidos.'})

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        first_name = request.POST.get('nome')
        last_name = request.POST.get('sobrenome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if request.POST.get("is_superuser"):
            superuser = True
        else:
            superuser = False
        user = User.objects.filter(username=username).first()
        if user:
            return render(request, 'register.html', {'error': 'ja existe um usuario com esse username'})
        elif password != password2:
            return render(request, 'register.html', {'error': 'Senhas não coincidem'})
        else:
            user = User.objects.create_user(first_name = first_name, last_name=last_name, username=username, email = email, password=password, is_superuser = superuser)
            user.save()
            return render(request, 'login.html')


        
@login_required(login_url='/auth/login/')
def deslogar(request):
    logout(request)
    return redirect(login)

@login_required(login_url="/auth/login/")
def perfil(request):
        return render(request, 'perfil.html')

@login_required(login_url="/auth/login/")
def address(request):
    address = Endereco.objects.filter(username = request.user.username)
    return render(request, 'address.html',{'address': address})


@login_required(login_url="/auth/login/")
def addressregister(request):
        return render(request, 'addressregister.html')

@login_required(login_url="/auth/login/")
def address_save(request):
    if request.method == "GET":
        return render(request, 'address.html')
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

        Endereco.objects.create(
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
         
    return redirect(address)