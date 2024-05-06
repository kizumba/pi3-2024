from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, HttpResponse

from .models import Equipe,Turma, Atitude, Missao, Equipe_Atitude, Equipe_Missao

from .forms import TurmasForm, EquipesForm, AtitudesForm, MissoesForm

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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
    
    return render(request, 'equipes.html',{'equipes':equipes})

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
    turmas = Turma.objects.all()
    equipes = Equipe.objects.all()
    atitudes = Atitude.objects.all()
    missoes = Missao.objects.all()

    equipe_atitudes = Equipe_Atitude.objects.all()
    equipe_missoes = Equipe_Missao.objects.all()

    context = {
        'turmas':turmas,
        'equipes':equipes,
        'atitudes':atitudes,
        'missoes':missoes,
        'equipe_atitudes':equipe_atitudes,
        'equipe_missoes':equipe_missoes
    }
    return render(request, 'aula.html',context=context)


# FORMULÁRIOS
def formturmas(request):
    lista_turmas = Turma.objects.all()

    if request.method == "GET":
        form = TurmasForm()

        context = {
            'form':form,
            'lista_turmas':lista_turmas
        }

        return render(request, 'formturmas.html', context=context)
    
    else:
        form = TurmasForm(request.POST)
        if form.is_valid():
            turma = form.save()
            form = TurmasForm()
    
        context = {
            'form':form,
            'lista_turmas':lista_turmas
        }

        return render(request, 'formturmas.html', context=context)

def turma_editar(request, id):
    context = {}

    obj = get_object_or_404(TurmasForm, id = id)
    
    form = TurmasForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    
    context["form"] = form

    return render(request, "turmaeditar.html", context)


def formequipes(request):
    lista_equipes = Equipe.objects.all()

    if request.method == "GET":
        form = EquipesForm()

        context = {
            'form':form,
            'lista_equipes':lista_equipes
        }

        return render(request, 'formequipes.html',context=context)
    
    else:
        form = EquipesForm(request.POST)
        if form.is_valid():
            equipe = form.save()
            form = EquipesForm()

        context = {
            'form':form,
            'lista_equipes':lista_equipes
        }

        return render(request, 'formequipes.html',context=context)

def formatitudes(request):
    lista_atitudes = Atitude.objects.all()

    if request.method == "GET":
        form = AtitudesForm

        context = {
            'form':form,
            'lista_atitudes':lista_atitudes
        }

        return render(request, 'formatitudes.html', context=context)
    
    else:
        form = AtitudesForm(request.POST)
        if form.is_valid():
            atitude = form.save()
            form = AtitudesForm()
        
        context = {
            'form':form,
            'lista_atitudes':lista_atitudes
        }

        return render(request, 'formatitudes.html', context=context)

def formmissoes(request):
    lista_missoes = Missao.objects.all()
    
    if request.method == "GET":
        form = MissoesForm

        context = {
            'form':form,
            'lista_missoes':lista_missoes
        }

        return render(request, 'formmissoes.html', context=context)
    
    else:
        form = MissoesForm(request.POST)
        if form.is_valid():
            missao = form.save()
            form = MissoesForm()
        
        context = {
            'form':form,
            'lista_missoes':lista_missoes
        }

        return render(request, 'formmissoes.html',context=context)

# TURMA CRUD

def create_turma(request):
    
    context = {}

    form = TurmasForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']=form
    return render(request, 'create_turma.html', context)

def list_turmas(request):
    context = {}

    context['dataset'] = Turma.objects.all()

    return render(request, "list_turmas.html", context)

def detail_turma(request, id_turma):

    context = {}

    context['data'] = Turma.objects.get(id_turma = id_turma)

    return render(request, "detail_turma.html", context)

def update_turma(request, id_turma):
    
    context = {
        'id':id_turma
    }

    obj = get_object_or_404(Turma, id_turma = id_turma)
    
    form = TurmasForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

        turmas = Turma.objects.all()

        return render(request, 'list_turmas.html', {'dataset':turmas})

    context['form'] = form

    return render(request, "update_turma.html", context)

def delete_turma(request, id_turma):

    context = {
        'id':id_turma
    }

    obj = get_object_or_404(Turma, id_turma = id_turma)

    if request.method == 'POST':
        obj.delete()
        
        turmas = Turma.objects.all()

        return render(request, 'list_turmas.html', {'dataset':turmas})
    
    return render(request, "delete_turma.html", context)

# EQUIPE CRUD