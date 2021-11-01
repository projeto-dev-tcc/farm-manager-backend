# Generated by Django 3.2.7 on 2021-11-01 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0002_auto_20211031_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adubo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=240, verbose_name='Nome')),
                ('data_hora_registrado', models.DateTimeField(auto_now_add=True, verbose_name='Horário Registrado')),
            ],
        ),
        migrations.CreateModel(
            name='AnotacaoConsultoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=340, verbose_name='Descricao')),
                ('litros_cova', models.FloatField(verbose_name='Litros por cova')),
                ('produtividade', models.FloatField(verbose_name='Produtividade por pé')),
                ('produtividade_sacas_hectare', models.FloatField(verbose_name='Produtividade em sacas por hectare')),
                ('data_hora_registrado', models.DateTimeField(auto_now_add=True, verbose_name='Horário registrado')),
                ('variedade', models.ManyToManyField(related_name='id_variedade_AnotacaoConsultoria', to='manager.Variedade')),
            ],
        ),
        migrations.CreateModel(
            name='TurmaColheita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('tipo', models.IntegerField(choices=[('MQ', 'Máquina'), ('MA', 'Mão')], verbose_name='Tipo de Serviço')),
                ('quantidade_colhida', models.FloatField(verbose_name='Valor da Viagem')),
                ('data_hora_registrado', models.DateTimeField(auto_now_add=True, verbose_name='Horário Registrado')),
            ],
        ),
        migrations.RemoveField(
            model_name='maquinario',
            name='horas_trabalhadas',
        ),
        migrations.RemoveField(
            model_name='servico',
            name='maquinario',
        ),
        migrations.RemoveField(
            model_name='servico',
            name='talhao',
        ),
        migrations.RemoveField(
            model_name='servico',
            name='usuario',
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=240, verbose_name='Nome')),
                ('valor_viagem', models.FloatField(max_length=240, verbose_name='Valor da Viagem')),
                ('data_hora_registrado', models.DateTimeField(auto_now_add=True, verbose_name='Horário Registrado')),
                ('turma_colheita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_turma_colheita_Turma', to='manager.servico')),
            ],
        ),
        migrations.CreateModel(
            name='ServicoMaquinario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_registrado', models.DateTimeField(auto_now_add=True, verbose_name='Horário Registrado')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_usuario_ServicoMaquinario', to=settings.AUTH_USER_MODEL)),
                ('maquinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_maquinario_ServicoMaquinario', to='manager.maquinario')),
                ('talhao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_talhao_ServicoMaquinario', to='manager.talhao')),
            ],
        ),
        migrations.CreateModel(
            name='QuantidadePlantio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(verbose_name='Quantidade')),
                ('data_hora_registrado', models.DateTimeField(auto_now_add=True, verbose_name='Horário Registrado')),
                ('variedade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_variedade_QuantidadePlantio', to='manager.variedade')),
            ],
        ),
        migrations.CreateModel(
            name='Plantio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_registrado', models.DateTimeField(auto_now_add=True, verbose_name='Horário Registrado')),
                ('quantidade_plantio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_plantio_Plantio', to='manager.quantidadeplantio')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_servico_Plantio', to='manager.servico')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaContratada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=240, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=240, verbose_name='Telefone')),
                ('data_hora_registrado', models.DateTimeField(auto_now_add=True, verbose_name='Horário Registrado')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_turma_PessoaContratada', to='manager.turma')),
            ],
        ),
        migrations.CreateModel(
            name='Fertilizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(verbose_name='Data de Inicio')),
                ('data_termino', models.DateField(verbose_name='Data de Término')),
                ('observacoes', models.TextField(verbose_name='Observações')),
                ('data_hora_registrado', models.DateTimeField(auto_now_add=True, verbose_name='Horário Registrado')),
                ('adubo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_adubo_Fertilizacao', to='manager.adubo')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_servico_Fertilizacao', to='manager.servico')),
            ],
        ),
        migrations.CreateModel(
            name='ConsultoriaAgronomo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('data_hora_registrado', models.DateTimeField(auto_now_add=True, verbose_name='Horário Registrado')),
                ('agronomo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_agronomo_ConsultoriaAgronomo', to=settings.AUTH_USER_MODEL)),
                ('anotacao_consultoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_anotacao_consultoria_ConsultoriaAgronomo', to='manager.anotacaoconsultoria')),
                ('fazenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_fazenda_ConsultoriaAgronomo', to='manager.fazenda')),
            ],
        ),
        migrations.CreateModel(
            name='Colheita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_registrado', models.DateTimeField(auto_now_add=True, verbose_name='Horário Registrado')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_servico_Colheita', to='manager.servico')),
                ('turma_colheita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_turma_colheita_Colheita', to='manager.turmacolheita')),
            ],
        ),
        migrations.AddField(
            model_name='servico',
            name='servico_maquinario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='id_servico_maquinario_Servico', to='manager.servicomaquinario'),
            preserve_default=False,
        ),
    ]
