# Generated by Django 4.2.11 on 2024-04-26 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atitude',
            fields=[
                ('id_atitude', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
                ('pontos', models.IntegerField()),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Missao',
            fields=[
                ('id_missao', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
                ('concluida', models.BooleanField()),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateField(auto_now=True)),
                ('data_finalizacao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id_turma', models.AutoField(primary_key=True, serialize=False)),
                ('serie', models.CharField(max_length=10)),
                ('periodo', models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=1)),
                ('data_criacao', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id_equipe', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('lider', models.CharField(max_length=30)),
                ('atitudes', models.ManyToManyField(blank=True, to='gamificacao.atitude')),
                ('missoes', models.ManyToManyField(blank=True, to='gamificacao.missao')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipes', to='gamificacao.turma')),
            ],
        ),
    ]
