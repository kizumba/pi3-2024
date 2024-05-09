from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, HttpResponse

from .models import Equipe,Turma, Atitude, Missao, Equipe_Atitude, Equipe_Missao

from .forms import TurmasForm, EquipesForm, AtitudesForm, MissoesForm

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Funções para chamar as páginas html
def index(request):
    return render(request, 'index.html')

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
def list_equipes(request):
    context = {}

    context['dataset'] = Equipe.objects.all()

    return render(request, "list_equipes.html", context)

def create_equipe(request):
    
    context = {}

    form = EquipesForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']=form
    return render(request, 'create_equipe.html', context)

def detail_equipe(request, id_equipe):

    context = {}

    context['data'] = Equipe.objects.get(id_equipe = id_equipe)

    return render(request, "detail_equipe.html", context)

def update_equipe(request, id_equipe):
    
    context = {
        'id':id_equipe
    }

    obj = get_object_or_404(Equipe, id_equipe = id_equipe)
    
    form = EquipesForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

        equipes = Equipe.objects.all()

        return render(request, 'list_equipes.html', {'dataset':equipes})

    context['form'] = form

    return render(request, "update_equipe.html", context)

def delete_equipe(request, id_equipe):

    context = {
        'id':id_equipe
    }

    obj = get_object_or_404(Equipe, id_equipe = id_equipe)

    if request.method == 'POST':
        obj.delete()
        
        equipes = Equipe.objects.all()

        return render(request, 'list_equipes.html', {'dataset':equipes})
    
    return render(request, "delete_equipe.html", context)

# ATITUDE CRUD
def list_atitudes(request):
    context = {}

    context['dataset'] = Atitude.objects.all()

    return render(request, "list_atitudes.html", context)

def create_atitude(request):
    
    context = {}

    form = AtitudesForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']=form
    return render(request, 'create_atitude.html', context)

def detail_atitude(request, id_atitude):

    context = {}

    context['data'] = Atitude.objects.get(id_atitude = id_atitude)

    return render(request, "detail_atitude.html", context)

def update_atitude(request, id_atitude):
    
    context = {
        'id':id_atitude
    }

    obj = get_object_or_404(Atitude, id_atitude = id_atitude)
    
    form = AtitudesForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

        atitudes = Atitude.objects.all()

        return render(request, 'list_atitudes.html', {'dataset':atitudes})

    context['form'] = form

    return render(request, "update_atitude.html", context)

def delete_atitude(request, id_atitude):

    context = {
        'id':id_atitude
    }

    obj = get_object_or_404(Atitude, id_atitude = id_atitude)

    if request.method == 'POST':
        obj.delete()
        
        atitudes = Atitude.objects.all()

        return render(request, 'list_atitudes.html', {'dataset':atitudes})
    
    return render(request, "delete_atitude.html", context)

# MISSÃO CRUD
def list_missoes(request):
    context = {}

    context['dataset'] = Missao.objects.all()

    return render(request, "list_missoes.html", context)

def create_missao(request):
    
    context = {}

    form = MissoesForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']=form
    return render(request, 'create_missao.html', context)

def detail_missao(request, id_missao):

    context = {}

    context['data'] = Missao.objects.get(id_missao = id_missao)

    return render(request, "detail_missao.html", context)

def update_missao(request, id_missao):
    
    context = {
        'id':id_missao
    }

    obj = get_object_or_404(Missao, id_missao = id_missao)
    
    form = MissoesForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

        missoes = Missao.objects.all()

        return render(request, 'list_missoes.html', {'dataset':missoes})

    context['form'] = form

    return render(request, "update_missao.html", context)

def delete_missao(request, id_missao):

    context = {
        'id':id_missao
    }

    obj = get_object_or_404(Missao, id_missao = id_missao)

    if request.method == 'POST':
        obj.delete()
        
        missoes = Missao.objects.all()

        return render(request, 'list_missoes.html', {'dataset':missoes})
    
    return render(request, "delete_missao.html", context)