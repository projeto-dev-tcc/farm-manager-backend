from django.db import models

class Fazenda(models.Model):
    nome = models.CharField("Nome", max_length=240)
    proprietario = models.ForeignKey("usuarios.Usuario", related_name="id_proprietario_Fazenda", on_delete=models.CASCADE)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Fazenda"
        verbose_name_plural = "Fazendas"
        app_label = 'manager'

    def __str__(self):
        return self.nome
    
class FuncionarioFazenda(models.Model):
    TIPO_CHOICES = (
        ("A", "Agrônomo"),
        ("F", "Funcionário"),
    )

    fazenda = models.ForeignKey(Fazenda, related_name="id_fazenda_FuncionarioFazenda", on_delete=models.CASCADE)
    funcionario = models.ForeignKey("usuarios.Usuario", related_name="id_funcionario_FuncionarioFazenda", on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, blank=False, null=False)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Funcionario da Fazenda"
        verbose_name_plural = "Funcionarios da Fazenda"
        app_label = 'manager'

    def __str__(self):
        return str(self.fazenda.nome + self.funcionario.nome)

class Maquinario(models.Model):
    TIPO_MAQUINARIO_CHOICE = [
        (1, "Trator"),
        (2, "Emplemento")
    ]

    fazenda = models.ForeignKey(Fazenda, related_name="id_fazenda_Maquinario", on_delete=models.CASCADE)
    tipo = models.IntegerField('Tipo de Maquinário', choices=TIPO_MAQUINARIO_CHOICE)
    marca = models.CharField("Marca", max_length=200)
    modelo = models.CharField("Modelo", max_length=200)
    ano_fabricacao = models.CharField("Ano", max_length=4, blank = True, null = True)
    data_aquisicao = models.DateField("Data de Aquisição", auto_now=False)
    observacoes = models.TextField("Observações", blank = True, null = True)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)
    
    class Meta:
        verbose_name = "Maquinário"
        verbose_name_plural = "Maquinários"
        app_label = 'manager'

    def __str__(self):
        return str(self.marca + self.modelo + self.ano)

class Variedade(models.Model):
    nome = models.CharField("Nome", max_length=240, unique=True)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Variedade"
        verbose_name_plural = "Variedades"
        app_label = 'manager'

    def __str__(self):
        return self.nome

class Talhao(models.Model):
    fazenda = models.ForeignKey(Fazenda, related_name="id_fazenda_Talhao", on_delete=models.CASCADE)
    variedade = models.ManyToManyField(Variedade, related_name="id_variedade_Talhao")
    nome = models.CharField("Nome", max_length=200)
    ano_plantio = models.CharField("Ano do plantio", max_length=10, blank=True, null=True)
    numero_covas = models.PositiveIntegerField("Numero de covas", blank=True, null=True)
    espacamento_rua = models.FloatField("Espaçamento das ruas", blank=True, null=True)
    espacamento_cova = models.FloatField("Espaçamento das covas", blank=True, null=True)
    area = models.FloatField("Área em hectare", blank=True, null=True)
    numero_covas_hectare = models.PositiveIntegerField("Número de covas por hectare", blank=True, null=True)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Talhao"
        verbose_name_plural = "Talhôes"
        app_label = 'manager'

    def __str__(self):
        return str(self.nome)

class ServicoMaquinario(models.Model):
    talhao = models.ForeignKey(Talhao, on_delete=models.CASCADE, related_name="id_talhao_ServicoMaquinario")
    funcionario = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE, related_name="id_funcionario_ServicoMaquinario")
    maquinario = models.ForeignKey(Maquinario, on_delete=models.CASCADE, related_name="id_maquinario_ServicoMaquinario")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Serviço do Maquinário"
        verbose_name_plural = "Serviços do Maquinário"
        app_label = 'manager'

    def __str__(self):
        return str(self.talhao.nome + self.funcionario.nome + self.maquinario.nome)

class Servico(models.Model):
    TIPO_SERVICO_CHOICE = [
        (1, "Plantio"),
        (2, "Fertilização"),
        (3, "Preparação do Solo"),
        (4, "Outros"),
    ]

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        app_label = 'manager'
    
    tipo = models.IntegerField('Tipo de Serviço', choices=TIPO_SERVICO_CHOICE)
    fazenda = models.ForeignKey(Fazenda, related_name="id_fazenda_Servico", on_delete=models.CASCADE)
    servico_maquinario = models.ForeignKey(ServicoMaquinario, on_delete=models.CASCADE, related_name="id_servico_maquinario_Servico")
    data_inicio = models.DateField("Data de Inicio", auto_now = False)
    data_termino = models.DateField("Data de Término", auto_now = False)
    observacoes = models.TextField("Observações")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    def __str__(self):
        return str(self.tipo)

class QuantidadePlantio(models.Model):
    variedade = models.ForeignKey(Variedade, on_delete=models.CASCADE, related_name="id_variedade_QuantidadePlantio")
    quantidade = models.PositiveIntegerField("Quantidade")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Quantidade do Plantio"
        verbose_name_plural = "Quantidade dos Plantios"
        app_label = 'manager'

    def __str__(self):
        return str(self.variedade + self.quantidade)

class Plantio(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name="id_servico_Plantio")
    quantidade_plantio = models.ForeignKey(QuantidadePlantio, on_delete=models.CASCADE, related_name="id_plantio_Plantio")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Plantio"
        verbose_name_plural = "Plantios"
        app_label = 'manager'

    def __str__(self):
        return str(self.servico)

class Adubo(models.Model):
    nome = models.CharField("Nome", max_length=240)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Adubo"
        verbose_name_plural = "Adubos"
        app_label = 'manager'

    def __str__(self):
        return self.nome

class Fertilizacao(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name="id_servico_Fertilizacao")
    adubo = models.ForeignKey(Adubo, on_delete=models.CASCADE, related_name="id_adubo_Fertilizacao")
    data_inicio = models.DateField("Data de Inicio", auto_now = False)
    data_termino = models.DateField("Data de Término", auto_now = False)
    observacoes = models.TextField("Observações")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Fertilização"
        verbose_name_plural = "Fertilizaçôes"
        app_label = 'manager'

    def __str__(self):
        return str(self.servico + self.adubo)

class TurmaColheita(models.Model):
    TIPO_COLHEITA_CHOICE = [
        ("MQ", "Máquina"),
        ("MA", "Mão"),
    ]
    data = models.DateField("Data", auto_now = False)
    tipo = models.IntegerField('Tipo de Serviço', choices=TIPO_COLHEITA_CHOICE)
    quantidade_colhida = models.FloatField("Valor da Viagem")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)
    
    class Meta:
        verbose_name = "Turma da Colheita"
        verbose_name_plural = "Turmas da Colheita"
        app_label = 'manager'

    def __str__(self):
        return str(self.data + self.tipo)

class Colheita(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name="id_servico_Colheita")
    turma_colheita = models.ForeignKey(TurmaColheita, on_delete=models.CASCADE, related_name="id_turma_colheita_Colheita")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Colheita"
        verbose_name_plural = "Colheitas"
        app_label = 'manager'

    def __str__(self):
        return str(self.servico + self.turma_colheita)

class Turma(models.Model):
    nome = models.CharField("Nome", max_length=240)
    valor_viagem = models.FloatField("Valor da Viagem", max_length=240)
    turma_colheita = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name="id_turma_colheita_Turma")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        app_label = 'manager'

    def __str__(self):
        return str(self.nome)

class PessoaContratada(models.Model):
    nome = models.CharField("Nome", max_length=240)
    telefone = models.CharField("Telefone", max_length=240)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="id_turma_PessoaContratada")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Pessoa Contratada"
        verbose_name_plural = "Pessoas Contratadas"
        app_label = 'manager'

    def __str__(self):
        return str(self.nome + self.telefone)

class AnotacaoConsultoria(models.Model):
    descricao = models.CharField("Descricao", max_length=340)
    variedade = models.ManyToManyField(Variedade, related_name="id_variedade_AnotacaoConsultoria")
    litros_cova = models.FloatField("Litros por cova")
    produtividade = models.FloatField("Produtividade por pé")
    produtividade_sacas_hectare = models.FloatField("Produtividade em sacas por hectare")
    data_hora_registrado = models.DateTimeField("Horário registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Anotação da Consultoria"
        verbose_name_plural = "Anotações da Consultoria"
        app_label = 'manager'

    def __str__(self):
        return str(self.descricao)

class ConsultoriaAgronomo(models.Model):
    agronomo = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE, related_name="id_agronomo_ConsultoriaAgronomo")
    data = models.DateField("Data", auto_now = False)
    fazenda = models.ForeignKey(Fazenda, related_name="id_fazenda_ConsultoriaAgronomo", on_delete=models.CASCADE)
    anotacao_consultoria = models.ForeignKey(AnotacaoConsultoria, related_name="id_anotacao_consultoria_ConsultoriaAgronomo", on_delete=models.CASCADE)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Consultoria do Agrônomo"
        verbose_name_plural = "Consultorias do Agrônomo"
        app_label = 'manager'

    def __str__(self):
        return str(self.agronomo + self.fazenda)
