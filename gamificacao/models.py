from django.db import models
from django.urls import reverse
from django.conf import settings

PERIODO = (('M','Manhã'),('T','Tarde'),('N','Noite'))

# Create your models here.
class Turma(models.Model):
    id_turma = models.AutoField(primary_key=True)
    serie = models.CharField(max_length=10, unique=True)
    periodo = models.CharField(choices=PERIODO,max_length=1)
    data_criacao = models.DateField(auto_now=True)

    def __str__(self):
        return f'Turma: Série: {self.serie}, período: {self.periodo} criada em {self.data_criacao}'
    
class Equipe(models.Model):
    id_equipe = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    lider = models.CharField(max_length=30)
    
    pontos = models.IntegerField(default=0)
    
    turma = models.ForeignKey(Turma, related_name='equipes', null=False, on_delete=models.CASCADE)    

    def __str__(self):
        return f'{self.nome}, Líder: {self.lider}, Pontos: {self.pontos} | Turma: {self.turma.serie}'


class Atitude(models.Model):
    id_atitude = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, unique=True)
    pontos = models.IntegerField()
    descricao = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'Atitude: {self.nome}, Descrição: {self.descricao}, Pontos: {self.pontos}'
    
    
class Missao(models.Model):
    id_missao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, unique=True)
    descricao = models.TextField(null=True, blank=True)
       
    def __str__(self):
        return f'{self.nome}, Descrição: {self.descricao}'


# TABELAS para relação MUITOS PARA MUITOS
class Equipe_Atitude(models.Model):
    id_eq_ati = models.AutoField(primary_key='True')
    data_criacao = models.DateField(auto_now=True)

    equipe = models.ForeignKey(Equipe, related_name='atitudes', null=True, on_delete=models.CASCADE)
    atitude = models.ForeignKey(Atitude, related_name='equipes', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.equipe.nome} | {self.atitude.nome}'

class Equipe_Missao(models.Model):
    id_eq_mi = models.AutoField(primary_key='True')
    data_hora = models.DateTimeField(auto_now=True)
    concluida = models.BooleanField(null=True)
    data_criacao = models.DateField(auto_now=True)
    data_finalizacao = models.DateField(null=True, blank=True)

    equipe = models.ForeignKey(Equipe, related_name='missoes', null=True, on_delete=models.CASCADE)
    missao = models.ForeignKey(Missao, related_name='equipes', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.equipe.nome} | {self.missao.nome}'

