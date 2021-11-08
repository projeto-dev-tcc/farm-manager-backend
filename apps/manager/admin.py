from manager.models import Variedade
from django.contrib import admin
from .models import *

admin.site.register(Fazenda)
admin.site.register(Talhao)
admin.site.register(FuncionarioFazenda)
admin.site.register(Maquinario)
admin.site.register(Variedade)
admin.site.register(ServicoMaquinario)
admin.site.register(Servico)
admin.site.register(QuantidadePlantio)
admin.site.register(Plantio)
admin.site.register(Adubo)
admin.site.register(TurmaColheita)
admin.site.register(Colheita)
admin.site.register(Turma)
admin.site.register(PessoaContratada)
admin.site.register(AnotacaoConsultoria)
admin.site.register(ConsultoriaAgronomo)