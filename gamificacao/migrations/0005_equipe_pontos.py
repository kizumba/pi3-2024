# Generated by Django 4.2.11 on 2024-04-30 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamificacao', '0004_alter_atitude_descricao_alter_missao_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='pontos',
            field=models.IntegerField(default=0),
        ),
    ]