from manager.models import Variedade
from django.contrib import admin
from .models import *

admin.site.register(Fazenda)
admin.site.register(Talhao)
admin.site.register(FuncionarioFazenda)
admin.site.register(Fertilizacao)
admin.site.register(Maquinario)
admin.site.register(Variedade)
admin.site.register(PrestacaoServico)
admin.site.register(Plantio)
admin.site.register(Adubo)
admin.site.register(ArquivoDigitalizado)
admin.site.register(Colheita)
admin.site.register(AnotacaoConsultoria)
admin.site.register(ConsultoriaAgronomo)