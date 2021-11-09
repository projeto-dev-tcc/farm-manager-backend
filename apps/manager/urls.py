from django.urls import path
from manager.views import *

urlpatterns = [
    # FAZENDA
    path("fazenda/registrar/", registrar_fazenda, name="registrar_fazenda"),
    path("fazenda/editar/<int:id_fazenda>/", editar_fazenda, name="editar_fazenda"),
    path("fazenda/painel/administrativo/<int:id_fazenda>/", painel_administrativo, name="painel_administrativo"),
    path("fazenda/visualizar/<int:id_fazenda>/", visualizar_fazenda, name="visualizar_fazenda"),
    path("fazenda/listar/", listar_fazendas, name="listar_fazendas"),
    path("fazenda/remover/<int:id_fazenda>/", remover_fazenda, name="remover_fazenda"),
    
    # MAQUINÁRIO
    path("fazenda/maquinario/registrar/<int:id_fazenda>/<int:id_tipo>/", registrar_maquinario, name="registrar_maquinario"),
    path("fazenda/maquinario/editar/<int:id_maquinario>/", editar_maquinario, name="editar_maquinario"),
    path("fazenda/maquinario/visualizar/<int:id_maquinario>/", visualizar_maquinario, name="visualizar_maquinario"),
    path("fazenda/maquinario/listar/<int:id_fazenda>/<int:id_tipo>/", listar_maquinarios, name="listar_maquinarios"),
    path("fazenda/maquinario/remover/<int:id_maquinario>/", remover_maquinario, name="remover_maquinario"),
    
    # TALHÕES
    path("fazenda/talhao/registrar/<int:id_fazenda>/", registrar_talhao, name="registrar_talhao"),
    path("fazenda/talhao/editar/<int:id_talhao>/", editar_talhao, name="editar_talhao"),
    path("fazenda/talhao/visualizar/<int:id_talhao>/", visualizar_talhao, name="visualizar_talhao"),
    path("fazenda/talhao/listar/<int:id_fazenda>/", listar_talhoes, name="listar_talhoes"),
    path("fazenda/talhao/remover/<int:id_talhao>/", remover_talhao, name="remover_talhao"),
    
    # FUNCIONARIOS FAZENDAS
    path("fazenda/funcionario/registrar/<int:id_fazenda>/", registrar_funcionario, name="registrar_funcionario"),
    path("fazenda/funcionario/editar/<int:id_funcionario_fazenda>/", editar_funcionario, name="editar_funcionario"),
    path("fazenda/funcionario/visualizar/<int:id_funcionario_fazenda>/", visualizar_funcionario, name="visualizar_funcionario"),
    path("fazenda/funcionario/listar/<int:id_fazenda>/", listar_funcionarios, name="listar_funcionarios"),
    path("fazenda/funcionario/remover/<int:id_funcionario_fazenda>/", remover_funcionario, name="remover_funcionario"),
    
    # VARIEDADE
    path("variedade/registrar/", registrar_variedade, name="registrar_variedade"),
    path("variedade/editar/<int:id_variedade>/", editar_variedade, name="editar_variedade"),
    path("variedade/visualizar/<int:id_variedade>/", visualizar_variedade, name="visualizar_variedade"),
    path("variedade/listar/", listar_variedades, name="listar_variedades"),
    path("variedade/remover/<int:id_variedade>/", remover_variedade, name="remover_variedade"),
    
    # ADUBO
    path("adubo/registrar/", registrar_adubo, name="registrar_adubo"),
    path("adubo/editar/<int:id_adubo>/", editar_adubo, name="editar_adubo"),
    path("adubo/visualizar/<int:id_adubo>/", visualizar_adubo, name="visualizar_adubo"),
    path("adubo/listar/", listar_adubos, name="listar_adubos"),
    path("adubo/remover/<int:id_adubo>/", remover_adubo, name="remover_adubo"),
    
    # CONSULTORIA AGRONOMO
    path("consultoria/registrar/<int:id_fazenda>/", registrar_consultoria, name="registrar_consultoria"),
    path("consultoria/editar/<int:id_consultoria_fazenda>/", editar_consultoria, name="editar_consultoria"),
    path("consultoria/visualizar/<int:id_consultoria_fazenda>/", visualizar_consultoria, name="visualizar_consultoria"),
    path("consultoria/painel/", painel_consultorias, name="painel_consultorias"),
    path("consultoria/listar/<int:id_fazenda>/", listar_consultorias, name="listar_consultorias"),
    path("consultoria/remover/<int:id_consultoria_fazenda>/", remover_consultoria, name="remover_consultoria"),

    # ANOTAÇÃO CONSULTORIA
    path("fazenda/funcionario/registrar/<int:id_fazenda>/", registrar_funcionario, name="registrar_funcionario"),
    path("fazenda/funcionario/editar/<int:id_funcionario_fazenda>/", editar_funcionario, name="editar_funcionario"),
    path("fazenda/funcionario/visualizar/<int:id_funcionario_fazenda>/", visualizar_funcionario, name="visualizar_funcionario"),
    path("fazenda/funcionario/listar/<int:id_fazenda>/", listar_funcionarios, name="listar_funcionarios"),
    path("fazenda/funcionario/remover/<int:id_funcionario_fazenda>/", remover_funcionario, name="remover_funcionario"),

    # SERVIÇO
    path("fazenda/servico/listar/<int:id_fazenda>", listar_servicos, name="listar_servicos"),
]