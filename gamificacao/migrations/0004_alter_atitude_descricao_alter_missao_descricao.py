# Generated by Django 4.2.11 on 2024-04-27 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamificacao', '0003_alter_atitude_descricao_alter_missao_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atitude',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='missao',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]