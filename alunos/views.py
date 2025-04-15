from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User.objects.filter(username=username).exists():
            print('Username já existe.')
            return render (request, 'cadastro.html')
        
        user = User.objects.create_user(
            username=username, 
            first_name = firstname, 
            last_name = lastname, 
            email=email, 
            password = senha)
        user.save()

        print('Cadastro realizado')
        return render (request, 'login.html')

def login(request):

    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        verificar_usuario = authenticate(username=username, password=senha)

        if (verificar_usuario != None):
            login_django(request, verificar_usuario)

            return redirect ('index')
        else:
            print('Usuário ou senha incorretos')
            return render (request, 'login.html')
