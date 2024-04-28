from django.shortcuts import render

from .models import Equipe


# Funções para chamar as páginas html
def index(request):
    equipes = Equipe.objects.all()
    return render(request, 'index.html',{'equipes':equipes})

def turmas(request):
    return render(request, 'turmas.html',{})

def equipes(request):
    return render(request, 'equipes.html', {})

def atitudes(request):
    return render(request, 'atitudes.html', {})

def missoes(request):
    return render(request, 'missoes.html', {})

def ajuda(request):
    return render(request, 'ajuda.html', {})

def sobre(request):
    return render(request, 'sobre.html', {})

def aula(request):
    return render(request, 'aula.html',{})