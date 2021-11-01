from manager.views import *
from django.urls import path
from rest_framework import routers

urlpatterns = [
    # FAZENDA
    # path('api/fazendas/', ListFazenda),
    # path('api/fazendas/<int:pk>', DetailFazenda),
    
    # FAZENDA
    path("fazenda/registrar/", registrar_fazenda, name="registrar_fazenda"),
    path("fazenda/editar/<int:id_fazenda>/", editar_fazenda, name="editar_fazenda"),
    path("fazenda/visualizar/<int:id_fazenda>/", visualizar_fazenda, name="visualizar_fazenda"),
    path("fazenda/listar/", listar_fazendas, name="listar_fazendas"),
    path("fazenda/remover/<int:id_fazenda>", remover_fazenda, name="remover_fazenda"),
    
    # VARIEDADE
    path("variedade/registrar/", registrar_variedade, name="registrar_variedade"),
    path("variedade/editar/<int:id_variedade>/", editar_variedade, name="editar_variedade"),
    path("variedade/visualizar/<int:id_variedade>/", visualizar_variedade, name="visualizar_variedade"),
    path("variedade/listar/", listar_variedades, name="listar_variedades"),
    path("variedade/remover/<int:id_variedade>", remover_variedade, name="remover_variedade"),
    
    # MAQUINÁRIO
    path("maquinario/registrar/", registrar_maquinario, name="registrar_maquinario"),
    path("maquinario/editar/<int:id_maquinario>/", editar_maquinario, name="editar_maquinario"),
    path("maquinario/visualizar/<int:id_maquinario>/", visualizar_maquinario, name="visualizar_maquinario"),
    path("maquinario/listar/<int:id_fazenda>", listar_maquinarios, name="listar_maquinarios"),
    path("maquinario/remover/<int:id_maquinario>", remover_maquinario, name="remover_maquinario"),
]