from django.db import models
from django.urls import reverse
from django.conf import settings

PERIODO = (('M','Manhã'),('T','Tarde'),('N','Noite'))

# Create your models here.
class Turma(models.Model):
    user = models.ForeignKey (
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    id_turma = models.AutoField(primary_key=True)
    serie = models.CharField(max_length=10)
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
    # atitudes = models.ManyToManyField(Atitude, null=True, blank=True)
    # missoes = models.ManyToManyField(Missao, null=True, blank=True)

    def __str__(self):
        return f'{self.nome}, Líder: {self.lider}, Pontos: {self.pontos} | Turma: {self.turma.serie}'


class Atitude(models.Model):
    id_atitude = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    pontos = models.IntegerField()
    descricao = models.TextField(null=True, blank=True)
    data_criacao = models.DateField(auto_now=True)

    equipe = models.ForeignKey(Equipe, related_name='atitudes', null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Atitude: {self.nome}, Descrição: {self.descricao}, Pontos: {self.pontos}, | Equipe {self.equipe.nome}'
    
    
class Missao(models.Model):
    id_missao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    concluida = models.BooleanField()
    descricao = models.TextField(null=True, blank=True)
    data_criacao = models.DateField(auto_now=True)
    data_finalizacao = models.DateField()

    equipe = models.ForeignKey(Equipe, related_name='missoes', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}, Descrição: {self.descricao}, Concluída: {self.concluida} | Equipe {self.equipe.nome}'

# def get_absolute_url(self):
#         return reverse('main:listar_turmas')
    
# def get_absolute_url(self):
#     return reverse('main:detalhes_turma')
