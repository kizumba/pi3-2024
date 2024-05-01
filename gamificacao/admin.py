from django.contrib import admin
from .models import Atitude, Missao, Turma, Equipe, Equipe_Atitude, Equipe_Missao
# Register your models here.

admin.site.register(Atitude)
admin.site.register(Missao)
admin.site.register(Turma)
admin.site.register(Equipe)
admin.site.register(Equipe_Missao)
admin.site.register(Equipe_Atitude)