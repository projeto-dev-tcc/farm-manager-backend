# Generated by Django 3.2.7 on 2021-11-05 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_alter_maquinario_data_aquisicao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinario',
            name='observacoes',
            field=models.TextField(blank=True, null=True, verbose_name='Observações'),
        ),
    ]
