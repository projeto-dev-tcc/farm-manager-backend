from django.shortcuts import render, redirect
from apps import usuarios
from .validate import validate_variedade
from .models import *
from .forms import *
from usuarios.validate import group_required
from django.contrib import messages
from usuarios.models import Usuario
from django.contrib.auth.decorators import login_required

GPAdmin = "Administrador"
GPCliente = "Cliente"

# FAZENDA
@login_required
def registrar_fazenda(request):
    form = FazendaForm()
    if request.method == "POST":
        form = FazendaForm(request.POST)
        if form.is_valid():
            fazenda = form.save(commit=False)
            fazenda.proprietario = request.user
            fazenda.save()
            messages.success(request, f"A fazenda foi registrada com sucesso!")
            return redirect('listar_fazendas')
    
    context = {
        'form': form,
        'action': "Registrar"
    }
    return render(request, "manager/fazenda/registrar_fazenda.html", context)

@login_required
def editar_fazenda(request, id_fazenda):
    fazenda = Fazenda.objects.get(id=id_fazenda)
    form = FazendaForm(instance=fazenda)
    if request.method == "POST":
        form = FazendaForm(request.POST, instance=fazenda)
        if form.is_valid():
            form.save()
            messages.success(request, f"A fazenda foi modificada com sucesso!")
            return redirect('visualizar_fazenda', id_fazenda=id_fazenda)

    context = {
        "form": form,
        "action": "Editar",
        "fazenda": fazenda
    }
    
    return render(request, "manager/fazenda/registrar_fazenda.html", context)

@login_required
def listar_fazendas(request):
    fazendas = Fazenda.objects.filter(proprietario__id=request.user.id)
    context = {
        'fazendas': fazendas,
    }
    
    return render(request, "manager/fazenda/listar_fazendas.html", context)

@login_required
def painel_administrativo(request, id_fazenda):
    fazenda = Fazenda.objects.get(id=id_fazenda)
    talhoes = Talhao.objects.filter(fazenda__id = fazenda.id)
    funcionarios = FuncionarioFazenda.objects.filter(fazenda__id = fazenda.id)
    tratores = Maquinario.objects.filter(fazenda__id = fazenda.id, tipo = 1)
    emplementos = Maquinario.objects.filter(fazenda__id = fazenda.id, tipo = 2)
    servicos = PrestacaoServico.objects.filter(talhao__fazenda__id = fazenda.id)
    consultorias = ConsultoriaAgronomo.objects.filter(fazenda__id = fazenda.id)

    context = {
        'fazenda': fazenda,
        "talhoes": talhoes,
        "funcionarios": funcionarios,
        "tratores": tratores,
        "emplementos": emplementos,
        "servicos": servicos,
        "consultorias": consultorias
    }

    return render(request, "manager/fazenda/painel_administrativo.html", context)

@login_required
def listar_consultoria_fazenda(request, id_fazenda):
    fazenda = Fazenda.objects.get(id=id_fazenda)
    consultorias = ConsultoriaAgronomo.objects.filter(fazenda__id = fazenda.id)

    context = {
        'fazenda': fazenda,
        "consultorias": consultorias,
    }

    return render(request, "manager/fazenda/listar_consultoria_fazenda.html", context)

@login_required
def visualizar_consultoria_fazenda(request, id_consultoria):
    consultoria = ConsultoriaAgronomo.objects.get(id = id_consultoria)
    anotacoes = AnotacaoConsultoria.objects.filter(consultoria__id = consultoria.id)

    context = {
        "consultoria": consultoria,
        "anotacoes": anotacoes,
    }

    return render(request, "manager/fazenda/visualizar_consultoria_fazenda.html", context)

@login_required
def visualizar_fazenda(request, id_fazenda):
    fazenda = Fazenda.objects.get(id=id_fazenda)
    context = {
        'fazenda': fazenda,
    }
    return render(request, "manager/fazenda/visualizar_fazenda.html", context)

@login_required
def remover_fazenda(request, id_fazenda):
    fazenda = Fazenda.objects.get(id=id_fazenda)
    fazenda.delete()
    messages.success(request, f"A fazenda foi removida com sucesso!")
    return redirect("listar_fazendas")



# MAQUIN??RIO
@login_required
def registrar_maquinario(request, id_fazenda, id_tipo):
    fazenda = Fazenda.objects.get(id = id_fazenda)
    form = MaquinarioForm()
    if request.method == "POST":
        form = MaquinarioForm(request.POST)
        if form.is_valid():
            maquinario = form.save(commit=False)
            maquinario.fazenda = fazenda
            maquinario.tipo = id_tipo
            maquinario.save()
            messages.success(request, f"O maquin??rio foi registrado com sucesso!")
            return redirect('listar_maquinarios', fazenda.id, id_tipo)
    
    context = {
        'form': form,
        'fazenda': fazenda,
        'action': "Registrar",
        'id_tipo': id_tipo,
    }
    return render(request, "manager/maquinario/registrar_maquinario.html", context)

@login_required
def editar_maquinario(request, id_maquinario):
    maquinario = Maquinario.objects.get(id=id_maquinario)
    form = MaquinarioForm(instance=maquinario)
    if request.method == "POST":
        form = MaquinarioForm(request.POST, instance=maquinario)
        if form.is_valid():
            form.save()
            messages.success(request, f"O maquin??rio foi modificado com sucesso!")
            return redirect('visualizar_maquinario', id_maquinario = id_maquinario)

    context = {
        "form": form,
        "action": "Editar",
        "maquinario": maquinario
    }
    
    return render(request, "manager/maquinario/registrar_maquinario.html", context)

@login_required
def listar_maquinarios(request, id_fazenda, id_tipo):
    fazenda = Fazenda.objects.get(id = id_fazenda)
    maquinarios = Maquinario.objects.filter(fazenda__id=id_fazenda, tipo=id_tipo)

    context = {
        "fazenda": fazenda,
        "maquinarios": maquinarios,
        "tipo_maquinario": id_tipo,
    }
    
    return render(request, "manager/maquinario/listar_maquinarios.html", context)

@login_required
def visualizar_maquinario(request, id_maquinario):
    maquinario = Maquinario.objects.get(id=id_maquinario)
    form = MaquinarioForm(instance=maquinario)

    context = {
        'maquinario': maquinario,
        'form': form
    }
    
    return render(request, "manager/maquinario/visualizar_maquinario.html", context)

@login_required
def remover_maquinario(request, id_maquinario):
    maquinario = Maquinario.objects.get(id=id_maquinario)
    maquinario.delete()
    messages.success(request, f"O maquin??rio foi removido com sucesso!")
    
    return redirect("listar_maquinarios", maquinario.fazenda.id, maquinario.tipo)



# TALH??O
@login_required
def registrar_talhao(request, id_fazenda):
    fazenda = Fazenda.objects.get(id = id_fazenda)
    form = TalhaoForm()
    if request.method == "POST":
        form = TalhaoForm(request.POST)
        if form.is_valid():
            talhao = form.save(commit=False)
            talhao.fazenda = fazenda
            talhao.save()

            # salvar many to many
            form.save_m2m()

            messages.success(request, f"O talh??o foi registrado com sucesso!")
            return redirect('listar_talhoes', id_fazenda)
    context = {
        'form': form,
        'action': "Registrar",
        'id_fazenda': id_fazenda
    }
    return render(request, "manager/talhao/registrar_talhao.html", context)

@login_required
def editar_talhao(request, id_talhao):
    talhao = Talhao.objects.get(id=id_talhao)
    form = TalhaoForm(instance=talhao)
    if request.method == "POST":
        form = TalhaoForm(request.POST, instance=talhao)
        if form.is_valid():
            form.save()
            messages.success(request, f"O talh??o foi modificado com sucesso!")
            return redirect('visualizar_talhao', id_talhao=id_talhao)

    context = {
        "form": form,
        "action": "Editar",
        "talhao": talhao
    }
    
    return render(request, "manager/talhao/registrar_talhao.html", context)

@login_required
def listar_talhoes(request, id_fazenda):
    fazenda = Fazenda.objects.get(id = id_fazenda)
    talhoes = Talhao.objects.filter(fazenda__id=id_fazenda)
     
    context = {
        'fazenda': fazenda,
        'talhoes': talhoes,
    }
    
    return render(request, "manager/talhao/listar_talhoes.html", context)

@login_required
def visualizar_talhao(request, id_talhao):
    talhao = Talhao.objects.get(id=id_talhao)
    context = {
        'talhao': talhao,
    }
    return render(request, "manager/talhao/visualizar_talhao.html", context)

@login_required
def remover_talhao(request, id_talhao):
    talhao = Talhao.objects.get(id=id_talhao)
    talhao.delete()
    messages.success(request, f"O talh??o foi removido com sucesso!")
    
    return redirect("listar_talhoes", talhao.fazenda.id)



# VARIEDADE
@login_required
def registrar_variedade(request):
    form = VariedadeForm()
    if request.method == "POST":
        form = VariedadeForm(request.POST)
        nome = request.POST.get('nome', None)
        if nome != "" and validate_variedade(nome):
            if form.is_valid():
                variedade = form.save(commit=False)
                variedade.nome = nome
                variedade.save()
                messages.success(request, f"A variedade foi registrada com sucesso no sistema!")
                return redirect('listar_variedades')
    context = {
        'form': form,
        'action': "Registrar"
    }
    return render(request, "manager/variedade/registrar_variedade.html", context)

@login_required
@group_required(GPAdmin)
def editar_variedade(request, id_variedade):
    variedade = Variedade.objects.get(id=id_variedade)
    form = VariedadeForm(instance=variedade)
    if request.method == "POST":
        form = VariedadeForm(request.POST, instance=variedade)
        if form.is_valid():
            form.save()
            messages.success(request, f"A variedade foi modificada com sucesso no sistema!")
            return redirect('visualizar_variedade', id_variedade)
    context = {
        "form": form,
        "action": "Editar",
        "variedade": variedade
    }
    
    return render(request, "manager/variedade/registrar_variedade.html", context)

@login_required
def listar_variedades(request):
    variedades = Variedade.objects.all()
    
    context = {
        'variedades': variedades,
        'messagem_screen': "Est??o sendo carregadas as variedades...",
    }
    
    return render(request, "manager/variedade/listar_variedades.html", context)

@login_required
def visualizar_variedade(request, id_variedade):
    variedade = Variedade.objects.get(id=id_variedade)
    form = VariedadeForm(instance=variedade)
    context = {
        'variedade': variedade,
        'form': form
    }
    
    return render(request, "manager/variedade/visualizar_variedade.html", context)

@login_required
def remover_variedade(request, id_variedade):
    variedade = Variedade.objects.get(id=id_variedade)
    variedade.delete()
    messages.success(request, f"A variedade foi removida com sucesso no sistema!")
    return redirect("listar_variedades")



# FUNCION??RIO FAZENDA
@login_required
def registrar_funcionario(request, id_fazenda):
    form = FuncionarioFazendaForm()
    fazenda = Fazenda.objects.get(id = id_fazenda)
    if request.method == "POST":
        form = FuncionarioFazendaForm(request.POST)
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.fazenda = fazenda
            if funcionario.tipo == "A":
                usuario = Usuario.objects.get(id = funcionario.funcionario.id)
                usuario.is_agronomo = True
                usuario.save()
            funcionario.save()
            messages.success(request, f"O funcion??rio foi registrado com sucesso no sistema!")
            return redirect('listar_funcionarios', id_fazenda)

    context = {
        'form': form,
        'action': "Registrar",
        'id_fazenda': id_fazenda
    }
    
    return render(request, "manager/funcionario/registrar_funcionario.html", context)

@login_required
def editar_funcionario(request, id_funcionario_fazenda):
    funcionario = FuncionarioFazenda.objects.get(id=id_funcionario_fazenda)
    form = FuncionarioFazendaForm(instance=funcionario)
    if request.method == "POST":
        form = FuncionarioFazendaForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            messages.success(request, f"O funcion??rio foi modificado com sucesso no sistema!")
            return redirect('visualizar_funcionario', id_funcionario_fazenda)
    context = {
        "form": form,
        "action": "Editar",
        "funcionario": funcionario
    }
    
    return render(request, "manager/funcionario/registrar_funcionario.html", context)

@login_required
def listar_funcionarios(request, id_fazenda):
    fazenda = Fazenda.objects.get(id = id_fazenda)
    funcionarios = FuncionarioFazenda.objects.filter(fazenda__id = fazenda.id)
    
    context = {
        'funcionarios': funcionarios,
        'messagem_screen': "Est??o sendo carregados os funcion??rios da fazenda...",
        'fazenda': fazenda
    }
    
    return render(request, "manager/funcionario/listar_funcionarios.html", context)

@login_required
def visualizar_funcionario(request, id_funcionario_fazenda):
    funcionario = FuncionarioFazenda.objects.get(id=id_funcionario_fazenda)
    form = FuncionarioFazendaForm(instance=funcionario)
    context = {
        'funcionario': funcionario,
        'form': form
    }
    
    return render(request, "manager/funcionario/visualizar_funcionario.html", context)

@login_required
def remover_funcionario(request, id_funcionario_fazenda):
    funcionario_fazenda = FuncionarioFazenda.objects.get(id=id_funcionario_fazenda)
    try:
        funcionario = Usuario.objects.get(id = funcionario_fazenda.funcionario.id)
        if funcionario_fazenda.tipo == "A":
            lista_fazendas = FuncionarioFazenda.objects.filter(funcionario__id = funcionario.id)
            if len(lista_fazendas) == 1:
                funcionario.is_agronomo = False
                funcionario.save()
    except:
        messages.error(request,"Ocorreu uma falha ao tentar remover o funcion??rio!")

    funcionario_fazenda.delete()
    messages.success(request, f"O funcion??rio {funcionario_fazenda.funcionario.nome} foi removido com sucesso no sistema!")
    return redirect("listar_funcionarios", funcionario_fazenda.fazenda.id)



# ADUBO
@login_required
def registrar_adubo(request):
    form = AduboForm()
    if request.method == "POST":
        form = AduboForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"O adubo foi registrado com sucesso no sistema!")
            return redirect('listar_adubos')
    context = {
        'form': form,
        'action': "Registrar"
    }
    return render(request, "manager/adubo/registrar_adubo.html", context)

@login_required
@group_required(GPAdmin)
def editar_adubo(request, id_adubo):
    adubo = Adubo.objects.get(id=id_adubo)
    form = AduboForm(instance=adubo)
    if request.method == "POST":
        form = AduboForm(request.POST, instance=adubo)
        if form.is_valid():
            form.save()
            messages.success(request, f"O adubo foi modificado com sucesso no sistema!")
            return redirect('visualizar_adubo', id_adubo)
    
    context = {
        "form": form,
        "action": "Editar",
        "adubo": adubo
    }
    
    return render(request, "manager/adubo/registrar_adubo.html", context)

@login_required
def listar_adubos(request):
    adubos = Adubo.objects.all()
    
    context = {
        'adubos': adubos,
        'messagem_screen': "Est??o sendo carregadas as adubos...",
    }
    
    return render(request, "manager/adubo/listar_adubos.html", context)

@login_required
def visualizar_adubo(request, id_adubo):
    adubo = Adubo.objects.get(id=id_adubo)
    form = AduboForm(instance=adubo)
    context = {
        'adubo': adubo,
        'form': form
    }
    
    return render(request, "manager/adubo/visualizar_adubo.html", context)

@login_required
def remover_adubo(request, id_adubo):
    adubo = Adubo.objects.get(id=id_adubo)
    adubo.delete()
    messages.success(request, f"O adubo foi removido com sucesso no sistema!")
    return redirect("listar_adubos")



# CONSULTORIA
@login_required
def registrar_consultoria(request, id_fazenda):
    form = ConsultoriaAgronomoForm()
    fazenda = Fazenda.objects.get(id = id_fazenda)
    if request.method == "POST":
        form = ConsultoriaAgronomoForm(request.POST)
        if form.is_valid():
            consultoria = form.save(commit=False)
            consultoria.fazenda = fazenda
            consultoria.agronomo = request.user
            consultoria.save()

            # salvar many to many
            form.save_m2m()

            messages.success(request, f"A consultoria foi registrada com sucesso no sistema!")
            return redirect('listar_consultorias', id_fazenda)

    context = {
        'form': form,
        'action': "Registrar",
        'id_fazenda': id_fazenda
    }
    
    return render(request, "manager/consultoria/registrar_consultoria.html", context)

@login_required
def editar_consultoria(request, id_consultoria):
    consultoria = ConsultoriaAgronomo.objects.get(id=id_consultoria)
    form = ConsultoriaAgronomoForm(instance=consultoria)
    if request.method == "POST":
        form = ConsultoriaAgronomoForm(request.POST, instance=consultoria)
        if form.is_valid():
            form.save()
            messages.success(request, f"A consultoria foi modificada com sucesso no sistema!")
            return redirect('visualizar_consultoria', id_consultoria)
    context = {
        "form": form,
        "action": "Editar",
        "consultoria": consultoria
    }
    
    return render(request, "manager/consultoria/registrar_consultoria.html", context)

@login_required
def listar_fazendas_consultoria(request):
    funcionario_fazenda = FuncionarioFazenda.objects.filter(funcionario = request.user)
    id_funcionario_fazenda = [ obj.fazenda.id for obj in funcionario_fazenda ]
    fazendas = Fazenda.objects.filter(id__in = id_funcionario_fazenda)
    context = {
        'fazendas': fazendas
    }

    return render(request, "manager/consultoria/listar_fazendas_consultoria.html", context)

@login_required
def listar_consultorias(request, id_fazenda):
    fazenda = Fazenda.objects.get(id = id_fazenda)
    consultorias = ConsultoriaAgronomo.objects.filter(fazenda__id = fazenda.id)

    context = {
        'consultorias': consultorias,
        'messagem_screen': "Est??o sendo carregados os funcion??rios da fazenda...",
        'fazenda': fazenda
    }
    
    return render(request, "manager/consultoria/listar_consultorias.html", context)

@login_required
def visualizar_consultoria(request, id_consultoria):
    consultoria = ConsultoriaAgronomo.objects.get(id=id_consultoria)
    anotacoes = AnotacaoConsultoria.objects.filter(consultoria__id = consultoria.id)
    context = {
        'consultoria': consultoria,
        'anotacoes': anotacoes
    }
    
    return render(request, "manager/consultoria/visualizar_consultoria.html", context)

@login_required
def remover_consultoria(request, id_consultoria):
    consultoria = ConsultoriaAgronomo.objects.get(id=id_consultoria)
    consultoria.delete()
    messages.success(request, f"A consultoria foi removida com sucesso no sistema!")
    return redirect("listar_consultorias", consultoria.fazenda.id)



# ANOTA????O
@login_required
def registrar_anotacao(request, id_consultoria):
    form = AnotacaoConsultoriaForm()
    consultoria = ConsultoriaAgronomo.objects.get(id = id_consultoria)
    if request.method == "POST":
        form = AnotacaoConsultoriaForm(request.POST)
        if form.is_valid():
            anotacao = form.save(commit=False)
            anotacao.consultoria = consultoria
            anotacao.save()

            messages.success(request, f"A anota????o foi registrada com sucesso no sistema!")
            return redirect('listar_anotacoes', consultoria.id)

    context = {
        'form': form,
        'action': "Registrar",
        'consultoria': consultoria
    }

    return render(request, "manager/anotacao/registrar_anotacao.html", context)

@login_required
def editar_anotacao(request, id_anotacao):
    anotacao = AnotacaoConsultoria.objects.get(id=id_anotacao)
    form = AnotacaoConsultoriaForm(instance=anotacao)
    if request.method == "POST":
        form = AnotacaoConsultoriaForm(request.POST, instance=anotacao)
        if form.is_valid():
            form.save()
            messages.success(request, f"A anota????o foi modificada com sucesso no sistema!")
            return redirect('visualizar_anotacao', id_anotacao)

    context = {
        "form": form,
        "action": "Editar",
        "anotacao": anotacao
    }
    
    return render(request, "manager/anotacao/registrar_anotacao.html", context)

@login_required
def visualizar_anotacao(request, id_anotacao):
    anotacao = AnotacaoConsultoria.objects.get(id=id_anotacao)
    context = {
        'anotacao': anotacao,
    }
    
    return render(request, "manager/anotacao/visualizar_anotacao.html", context)

@login_required
def listar_anotacoes(request, id_consultoria):
    consultoria = ConsultoriaAgronomo.objects.get(id = id_consultoria)
    anotacoes = AnotacaoConsultoria.objects.filter(consultoria__id = consultoria.id)

    context = {
        'anotacoes': anotacoes,
        'consultoria': consultoria,
        'messagem_screen': "Est??o sendo carregados os funcion??rios da fazenda...",
    }
    
    return render(request, "manager/anotacao/listar_anotacoes.html", context)

@login_required
def remover_anotacao(request, id_anotacao):
    anotacao = AnotacaoConsultoria.objects.get(id=id_anotacao)
    anotacao.delete()
    messages.success(request, f"A anota????o foi removida com sucesso no sistema!")
    return redirect("listar_anotacoes", anotacao.consultoria.id)



# SERVI??OS
@login_required
def listar_servicos(request, id_fazenda):
    fazenda = Fazenda.objects.get(id = id_fazenda)
    listServicos = PrestacaoServico.objects.filter(talhao__fazenda__id=id_fazenda).order_by("status")

    context = {
        'messagem_screen': "Est??o sendo carregados os servi??os da fazenda...",
        'fazenda': fazenda,
        'listServicos': listServicos
    }
    
    return render(request, "manager/servico/listar_servicos.html", context)

@login_required
def cadastrarServico(request, id_fazenda):
    fazenda = Fazenda.objects.get(id = id_fazenda)
    tratores = Maquinario.objects.filter(fazenda__id = fazenda.id, tipo = 1)
    implementos = Maquinario.objects.filter(fazenda__id = fazenda.id, tipo = 2)
    listVariedade = Variedade.objects.all()
    listAdubo = Adubo.objects.all()
    
    form = PrestacaoServicoForm()
    if request.method == "POST":
        form = PrestacaoServicoForm(request.POST)
        if form.is_valid():
            objPrestacaoServico = form.save()
            objPrestacaoServico.save()
            if objPrestacaoServico.tipo == 1:
                quantidade = request.POST.get('QuantidadePlantio', None)
                
                plantio = Plantio()
                plantio.prestacao_servico = objPrestacaoServico
                plantio.quantidade = int(quantidade)
                plantio.save()
            
            elif objPrestacaoServico.tipo == 2:
                id_adubo = request.POST.get('id_objFertilizacao', None)
                dosagem = request.POST.get('DosagemFertilizacao', None)
                adubo = Adubo.objects.get(id = int(id_adubo))
                
                fertilizacao = Fertilizacao()
                fertilizacao.prestacao_servico = objPrestacaoServico
                fertilizacao.adubo = adubo
                fertilizacao.dosagem = dosagem
                fertilizacao.save()
            else:
                tipo = request.POST.get('tipoColheita', None)
                quantidade = request.POST.get('QuantidadeColheita', None)
                colheita = Colheita()
                colheita.prestacao_servico = objPrestacaoServico
                colheita.tipo = tipo
                if quantidade:
                    colheita.quantidade = quantidade
                colheita.save()
                
        messages.success(request, f"Presta????o de servi??o cadastrado com sucesso!!!")
        return redirect('listar_servicos', fazenda.id)

    context = {
        'messagem_screen': "",
        'fazenda': fazenda,
        'form':form,
        'action': "Registrar",
        'listVariedade':listVariedade,
        'listAdubo':listAdubo,
        'tratores': tratores,
        'implementos': implementos,
    }
    
    return render(request, "manager/servico/registrar_servico.html", context)

@login_required
def editar_servico(request, id_servico):
    listVariedade = Variedade.objects.all()
    listAdubo = Adubo.objects.all()
    prestacao_servico = PrestacaoServico.objects.get(id=id_servico)
    tratores = Maquinario.objects.filter(fazenda__id = prestacao_servico.talhao.fazenda.id, tipo = 1)
    implementos = Maquinario.objects.filter(fazenda__id = prestacao_servico.talhao.fazenda.id, tipo = 2)
    form = PrestacaoServicoForm(instance=prestacao_servico)
    if request.method == "POST":
        form = PrestacaoServicoForm(request.POST, instance=prestacao_servico)
        if form.is_valid():
            form.save()
            messages.success(request, f"O servi??o foi modificado com sucesso no sistema!")
            return redirect('visualizar_servico', id_servico)
    context = {
        "form": form,
        "action": "Editar",
        'fazenda': prestacao_servico.talhao.fazenda,
        'listVariedade':listVariedade,
        'listAdubo':listAdubo,
        'tratores': tratores,
        'implementos': implementos,
    }
    
    return render(request, "manager/servico/registrar_servico.html", context)


@login_required
def visualizar_servico(request, id_servico):
    prestacao_servico = PrestacaoServico.objects.get(id=id_servico)
    if prestacao_servico.tipo == 1:
        tipo_servico = Plantio.objects.get(prestacao_servico__id = prestacao_servico.id)
    elif prestacao_servico.tipo == 2:
        tipo_servico = Fertilizacao.objects.get(prestacao_servico__id = prestacao_servico.id)
    else:
        tipo_servico = Colheita.objects.get(prestacao_servico__id = prestacao_servico.id)

    context = {
        'prestacao_servico': prestacao_servico,
        'tipo_servico': tipo_servico
    }
    
    return render(request, "manager/servico/visualizar_servico.html", context)

@login_required
def concluir_servico(request, id_servico):
    prestacao_servico = PrestacaoServico.objects.get(id=id_servico)
    if prestacao_servico.status == "C":
        messages.error(request, f"O servico j?? foi conclu??do!")
        return redirect("visualizar_servico", prestacao_servico.id)
    else:
        prestacao_servico.status = "C"
        prestacao_servico.save()
        messages.success(request, f"O servico foi conclu??do com sucesso!")
        return redirect("visualizar_servico", prestacao_servico.id)

@login_required
def remover_servico(request, id_servico):
    prestacao_servico = PrestacaoServico.objects.get(id=id_servico)
    prestacao_servico.delete()
    messages.success(request, f"O servico foi removido com sucesso no sistema!")
    return redirect("listar_servicos", prestacao_servico.talhao.fazenda.id)