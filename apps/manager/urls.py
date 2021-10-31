from manager.views import *
from django.urls import path
from rest_framework import routers

urlpatterns = [
    # FAZENDA
    # path('api/fazendas/', ListFazenda),
    # path('api/fazendas/<int:pk>', DetailFazenda),
    
    # VARIEDADE
    path("variedade/registrar/", registrar_variedade, name="registrar_variedade"),
    path("variedade/editar/<int:id_variedade>/", editar_variedade, name="editar_variedade"),
    path("variedade/visualizar/<int:id_variedade>/", visualizar_variedade, name="visualizar_variedade"),
    path("variedade/listar/", listar_variedades, name="listar_variedades"),
]