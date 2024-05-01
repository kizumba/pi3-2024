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
    path('formturmas', views.formturmas, name='formturmas'),
    path('formrequipes', views.formequipes, name='formequipes'),
    path('formatitudes',views.formatitudes, name='formatitudes'),
    path('formmissoes',views.formmissoes, name='formmissoes')
]