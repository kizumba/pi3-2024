from django.test import TestCase
from django.urls import reverse

from gamificacao.forms import TurmasForm

class TestarPaginas(TestCase):
    def testar_se_pagina_principal_carrega_completamente(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def testar_se_pagina_ajuda_carrega_template(self):
        response = self.client.get(reverse('ajuda'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        
    def testar_se_pagina_sobre_carrega_conteudo(self):
        response = self.client.get(reverse('sobre'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Sobre</h1>')

    def testar_se_pagina_sala_de_aula_nao_contem_conteudo(self):
        response = self.client.get(reverse('aula'))
        self.assertNotContains(response, 'Terraplanismo')

class TestarTurmaForm(TestCase):
    def testar_turma_form_valido(self):
        form = TurmasForm (
            data = {
                'serie':'UNIVESP',
                'periodo':'N'
            }
        )
        self.assertTrue(form.is_valid())
    
    def test_turma_form_invalido(self):
        form = TurmasForm(data={})
        self.assertFalse(form.is_valid())

