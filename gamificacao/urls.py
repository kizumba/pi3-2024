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
    path('formmissoes',views.formmissoes, name='formmissoes'),

    # update
    

    # Turma
    path('create_turma', views.create_turma, name='create_turma'),
    path('list_turmas', views.list_turmas, name='list_turmas'),
    path('detail_turma/<int:id_turma>/', views.detail_turma, name='detail-turma'),
    path('update_turma/<int:id_turma>', views.update_turma, name='update-turma'),
    path('delete_turma/<int:id_turma>', views.delete_turma, name='delete-turma'),

    # Equipe
    path('list_equipes', views.list_equipes, name='list_equipes'),
    path('create_equipe', views.create_equipe, name='create_equipe'),
    path('detail_equipe/<int:id_equipe>/', views.detail_equipe, name='detail-equipe'),
    path('update_equipe/<int:id_equipe>', views.update_equipe, name='update-equipe'),
    path('delete_equipe/<int:id_equipe>', views.delete_equipe, name='delete-equipe'),

    # Atitude
    path('list_atitudes', views.list_atitudes, name='list_atitudes'),
    path('create_atitude', views.create_atitude, name='create_atitude'),
    path('detail_atitude/<int:id_atitude>/', views.detail_atitude, name='detail-atitude'),
    path('update_atitude/<int:id_atitude>', views.update_atitude, name='update-atitude'),
    path('delete_atitude/<int:id_atitude>', views.delete_atitude, name='delete-atitude'),

    # Missão
    path('list_missoes', views.list_missoes, name='list_missoes'),
    path('create_missao', views.create_missao, name='create_missao'),
    path('detail_missao/<int:id_missao>/', views.detail_missao, name='detail-missao'),
    path('update_missao/<int:id_missao>', views.update_missao, name='update-missao'),
    path('delete_missao/<int:id_missao>', views.delete_missao, name='delete-missao'),
]