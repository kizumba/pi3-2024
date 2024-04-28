from django.shortcuts import render

from .models import Equipe,Turma, Atitude, Missao


# Funções para chamar as páginas html
def index(request):
    turmas = Turma.objects.all()
    equipes = Equipe.objects.all()
    atitudes = Atitude.objects.all()
    missoes = Missao.objects.all()

    return render(request, 'index.html',{
            'turmas':turmas,
            'equipes':equipes,
            'atitudes':atitudes,
            'missoes':missoes
        })

def turmas(request):
    turmas = Turma.objects.all()

    return render(request, 'turmas.html',{'turmas':turmas})

def equipes(request):
    equipes = Equipe.objects.all()

    return render(request, 'equipes.html', {'equipes':equipes})

def atitudes(request):
    atitudes = Atitude.objects.all()

    return render(request, 'atitudes.html', {'atitudes':atitudes})

def missoes(request):
    missoes = Missao.objects.all()

    return render(request, 'missoes.html', {'missoes':missoes})

def ajuda(request):
    return render(request, 'ajuda.html', {})

def sobre(request):
    return render(request, 'sobre.html', {})

def aula(request):
    return render(request, 'aula.html',{})


# CADASTROS
def cadastrar_turmas(request):
    turma = Turma

    return render(request, 'cadastrarturmas.html')

def cadastrar_equipes(request):
    return render(request, 'cadastrarequipes.html')

def cadastrar_atitudes(request):
    return render(request, 'cadastraratitudes.html')

def cadastrar_missoes(request):
    return render(request, 'cadastrarmissoes.html')