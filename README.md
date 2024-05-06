# pi3-2024
# Projeto Integrador 3 - 2024.

- **Como fazer deploy** https://www.youtube.com/watch?v=j6hsnVyjczA

- **Repositório** https://github.com/kizumba/pi3-2024.git

- **Site** https://kizumba.pythonanywhere.com

- **Python anywhere** https://www.pythonanywhere.com/user/kizumba/

# Pythonanywhere
Os comandos a seguir são executados no bash do pythonanywhere

- Instalar: `pip install --user pythonanywhere`
- Configurar: `pa_autoconfigure_django.py https://github.com/kizumba/pi3-2024.git --python=3.9 --nuke`
- Atualizar repositório: `git pull`
- Atualizar aplicação: `touch /var/www/kizumba_pythonanywhere_com_wsgi.py`
- Criar super usuário: `./manage.py createsuperuser`

# Lista de Tarefas
1. Criar as funções das páginas no view.py
2. Criar os caminhos das páginas no urls.py
3. Criar os links das páginas em indes.html

# Vídeos úteis
- Como usar pythonanywhere https://www.youtube.com/watch?v=j6hsnVyjczA 
- Como criar formulários em django https://www.youtube.com/watch?v=RGxYlL2Dm54