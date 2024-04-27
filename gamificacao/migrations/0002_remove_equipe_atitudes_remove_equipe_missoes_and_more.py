# Generated by Django 4.2.11 on 2024-04-26 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamificacao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='atitudes',
        ),
        migrations.RemoveField(
            model_name='equipe',
            name='missoes',
        ),
        migrations.AddField(
            model_name='atitude',
            name='equipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='atitudes', to='gamificacao.equipe'),
        ),
        migrations.AddField(
            model_name='missao',
            name='equipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='missoes', to='gamificacao.equipe'),
        ),
    ]
