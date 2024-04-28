from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),    
    path('turmas', views.turmas, name='turmas'),
    path('equipes', views.equipes, name='equipes'),
    path('atitudes', views.atitudes, name='atitudes'),
    path('missoes', views.missoes, name='missoes'),
    path('ajuda', views.ajuda, name='ajuda'),
    path('sobre', views.sobre, name='sobre'),
    path('aula', views.aula, name='aula'),

    # telas de cadastro
    path('cadastrarturmas', views.cadastrar_turmas, name='cadastrarturmas'),
    path('cadastrarequipes', views.cadastrar_equipes, name='cadastrarequipes'),
    path('cadastraratitudes',views.cadastrar_atitudes, name='cadastraratitudes'),
    path('cadastrarmissoes',views.cadastrar_missoes, name='cadastrarmissoes')
]