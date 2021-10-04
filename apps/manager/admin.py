from manager.models import Variedade
from django.contrib import admin
from .models import *

admin.site.register(Fazenda)
admin.site.register(Maquinario)
admin.site.register(Variedade)
admin.site.register(Talhao)
admin.site.register(Servico)