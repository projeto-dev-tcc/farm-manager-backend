from django.urls import path
from manager.views import *
from .validate import * 

urlpatterns = [
    # FAZENDA
    path("fazenda/registrar/", registrar_fazenda, name="registrar_fazenda"),
    path("fazenda/editar/<int:id_fazenda>/", editar_fazenda, name="editar_fazenda"),
    path("fazenda/painel/administrativo/<int:id_fazenda>/", painel_administrativo, name="painel_administrativo"),
    path("fazenda/visualizar/<int:id_fazenda>/", visualizar_fazenda, name="visualizar_fazenda"),
    path("fazenda/listar/consultoria/<int:id_fazenda>/", listar_consultoria_fazenda, name="listar_consultoria_fazenda"),
    path("fazenda/visualizar/consultoria/<int:id_consultoria>/", visualizar_consultoria_fazenda, name="visualizar_consultoria_fazenda"),
    path("fazenda/listar/", listar_fazendas, name="listar_fazendas"),
    path("fazenda/remover/<int:id_fazenda>/", remover_fazenda, name="remover_fazenda"),
    
    # MAQUINÁRIO
    path("fazenda/maquinario/registrar/<int:id_fazenda>/<int:id_tipo>/", registrar_maquinario, name="registrar_maquinario"),
    path("fazenda/maquinario/editar/<int:id_maquinario>/", editar_maquinario, name="editar_maquinario"),
    path("fazenda/maquinario/visualizar/<int:id_maquinario>/", visualizar_maquinario, name="visualizar_maquinario"),
    path("fazenda/maquinario/listar/<int:id_fazenda>/<int:id_tipo>/", listar_maquinarios, name="listar_maquinarios"),
    path("fazenda/maquinario/remover/<int:id_maquinario>/", remover_maquinario, name="remover_maquinario"),
    path("fazenda/maquinario/cadastrar/ajax/", Ajax_cadastrar_maquinario, name="Ajax_cadastrar_maquinario"),

    # TALHÕES
    path("fazenda/talhao/registrar/<int:id_fazenda>/", registrar_talhao, name="registrar_talhao"),
    path("fazenda/talhao/editar/<int:id_talhao>/", editar_talhao, name="editar_talhao"),
    path("fazenda/talhao/visualizar/<int:id_talhao>/", visualizar_talhao, name="visualizar_talhao"),
    path("fazenda/talhao/listar/<int:id_fazenda>/", listar_talhoes, name="listar_talhoes"),
    path("fazenda/talhao/remover/<int:id_talhao>/", remover_talhao, name="remover_talhao"),
    path("fazenda/talhao/registrar/ajax/", Ajax_cadastrar_talhao, name="Ajax_cadastrar_talhao"),
    
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
    path("adubo/registrar/ajax/", Ajax_cadastrar_adubo, name="Ajax_cadastrar_adubo"),
    
    # CONSULTORIA AGRONOMO
    path("consultoria/registrar/<int:id_fazenda>/", registrar_consultoria, name="registrar_consultoria"),
    path("consultoria/editar/<int:id_consultoria>/", editar_consultoria, name="editar_consultoria"),
    path("consultoria/visualizar/<int:id_consultoria>/", visualizar_consultoria, name="visualizar_consultoria"),
    path("consultoria/painel/", listar_fazendas_consultoria, name="listar_fazendas_consultoria"),
    path("consultoria/listar/<int:id_fazenda>/", listar_consultorias, name="listar_consultorias"),
    path("consultoria/remover/<int:id_consultoria>/", remover_consultoria, name="remover_consultoria"),

    # ANOTAÇÃO CONSULTORIA
    path("consultoria/anotacao/registrar/<int:id_consultoria>/", registrar_anotacao, name="registrar_anotacao"),
    path("consultoria/anotacao/editar/<int:id_anotacao>/", editar_anotacao, name="editar_anotacao"),
    path("consultoria/anotacao/visualizar/<int:id_anotacao>/", visualizar_anotacao, name="visualizar_anotacao"),
    path("consultoria/anotacao/listar/<int:id_consultoria>/", listar_anotacoes, name="listar_anotacoes"),
    path("consultoria/anotacao/remover/<int:id_anotacao>/", remover_anotacao, name="remover_anotacao"),

    # SERVIÇO
    path("fazenda/servico/listar/<int:id_fazenda>", listar_servicos, name="listar_servicos"),
    path("fazenda/servico/registrar/<int:id_fazenda>", cadastrarServico, name="cadastrarServico"),
    path("fazenda/servico/visualizar/<int:id_servico>", visualizar_servico, name="visualizar_servico"),
    path("fazenda/servico/editar/<int:id_servico>", editar_servico, name="editar_servico"),
    path("fazenda/servico/concluir/<int:id_servico>", concluir_servico, name="concluir_servico"),
    path("fazenda/servico/remover/<int:id_servico>", remover_servico, name="remover_servico"),
]