# Generated by Django 4.2.11 on 2024-04-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamificacao', '0006_remove_atitude_equipe_remove_missao_equipe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missao',
            name='data_finalizacao',
            field=models.DateField(blank=True, null=True),
        ),
    ]
