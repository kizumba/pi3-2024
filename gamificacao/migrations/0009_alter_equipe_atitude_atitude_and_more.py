# Generated by Django 4.2.11 on 2024-05-01 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamificacao', '0008_alter_atitude_nome_alter_equipe_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe_atitude',
            name='atitude',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipes', to='gamificacao.atitude'),
        ),
        migrations.AlterField(
            model_name='equipe_atitude',
            name='equipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='atitudes', to='gamificacao.equipe'),
        ),
        migrations.AlterField(
            model_name='equipe_missao',
            name='equipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='missoes', to='gamificacao.equipe'),
        ),
    ]
