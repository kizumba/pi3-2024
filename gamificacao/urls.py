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
    

    # NOVAS FUNÇÕES
    path('create_turma', views.create_turma, name='create_turma'),
    path('list_turmas', views.list_turmas, name='list_turmas'),
    path('detail_turma/<int:id_turma>/', views.detail_turma, name='detail-turma'),
    path('update_turma/<int:id_turma>', views.update_turma, name='update-turma'),
    path('delete_turma/<int:id_turma>', views.delete_turma, name='delete-turma')
]