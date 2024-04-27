from django.shortcuts import render

from .models import Equipe

def index(request):
    equipes = Equipe.objects.all()
    return render(request, 'index.html',{'equipes':equipes})