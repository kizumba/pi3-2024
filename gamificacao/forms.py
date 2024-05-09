from django import forms
from .models import Turma, Equipe, Atitude, Missao, Equipe_Atitude, Equipe_Missao

PERIODO = (('M','Manhã'),('T','Tarde'),('N','Noite'))

class TurmasForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ["serie", "periodo"]

class EquipesForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ["nome", "lider","pontos","turma"]

class AtitudesForm(forms.ModelForm):
    class Meta:
        model = Atitude
        fields = ["nome","pontos","descricao"]

class MissoesForm(forms.ModelForm):
    class Meta:
        model = Missao
        fields = ["nome","descricao"]

