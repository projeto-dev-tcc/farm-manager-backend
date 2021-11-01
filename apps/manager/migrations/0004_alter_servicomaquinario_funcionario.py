# Generated by Django 3.2.7 on 2021-11-01 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0003_auto_20211101_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicomaquinario',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_funcionario_ServicoMaquinario', to=settings.AUTH_USER_MODEL),
        ),
    ]
