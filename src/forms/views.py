from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpRequest
from .forms import formModels
from .models import dataFormModels
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def createMessageView(request: HttpRequest):
    if request.method == 'POST':
        myForm = formModels(request.POST)
        if myForm.is_valid():
            myForm.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('forms:Home')
        else:
            messages.error(request, 'Erro ao enviar mensagem. Verifique os campos.')
            context = {"form": myForm}
            return render(request, 'homePage/index.html', context)
    
    context = {
        "form": formModels()
    }
    return render(request, 'homePage/index.html', context)

@login_required(login_url='forms:login')
def getAllMessagesView(request):
    context = {
        "forms":dataFormModels.objects.all()
    }
    return render(request, 'adminPanel/adminPanel.html', context)

@login_required(login_url='forms:login')
def deleteMessageByIdView(request:HttpRequest, id):
    form = get_object_or_404(dataFormModels, id=id)
    form.delete()
    return redirect('forms:mensagens')

@login_required(login_url='forms:login')
def editMessageByIdView(request: HttpRequest, id):
    form_instance = get_object_or_404(dataFormModels, id=id)
    
    if request.method == "POST":
        form_obj = formModels(request.POST, instance=form_instance)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('forms:mensagens')
    else:
        form_obj = formModels(instance=form_instance)
    
    context = {
        'form': form_obj
    }
    return render(request, 'editForm/editMessage.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('forms:mensagens')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            
    return render(request, 'login/login.html')

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'As senhas não conferem.')
            return render(request, 'login/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
            return render(request, 'login/register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
        return redirect('forms:login')
        
    return render(request, 'login/register.html')