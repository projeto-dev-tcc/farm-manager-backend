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
        return self.funcionario.nome

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
    observacoes = models.TextField("Observações", blank = True, null = True)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)
    
    class Meta:
        verbose_name = "Maquinário"
        verbose_name_plural = "Maquinários"
        app_label = 'manager'

    def __str__(self):
        return str(self.marca + " " + self.modelo)

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
    nome = models.CharField("Nome", max_length=200)
    ano_plantio = models.CharField("Ano do plantio", max_length=10, blank=True, null=True)
    numero_covas = models.PositiveIntegerField("Numero de covas", blank=True, null=True)
    espacamento_rua = models.FloatField("Espaçamento das ruas", blank=True, null=True)
    espacamento_cova = models.FloatField("Espaçamento das covas", blank=True, null=True)
    area = models.FloatField("Área em hectare", blank=True, null=True)
    numero_covas_hectare = models.PositiveIntegerField("Número de covas por hectare", blank=True, null=True)
    variedade = models.ManyToManyField(Variedade, related_name="id_variedade_Talhao")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Talhao"
        verbose_name_plural = "Talhôes"
        app_label = 'manager'

    def __str__(self):
        return str(self.nome)

class Adubo(models.Model):
    nome = models.CharField("Nome", max_length=240)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Adubo"
        verbose_name_plural = "Adubos"
        app_label = 'manager'

    def __str__(self):
        return self.nome

class PrestacaoServico(models.Model):
    TIPO_SERVICO_CHOICE = [
        (1, "Plantio"),
        (2, "Fertilização"),
        (3, "Colheita"),
    ]

    STATUS_CHOICE = [
        ("A", "Andamento"),
        ("C", "Concluído")
    ]

    talhao = models.ForeignKey(Talhao, on_delete=models.CASCADE, related_name="id_talhao_ServicoMaquinario")
    funcionario = models.ForeignKey("usuarios.Usuario",  on_delete=models.CASCADE, related_name="id_funcionario_ServicoMaquinario")
    trator = models.ForeignKey(Maquinario,  on_delete=models.CASCADE, related_name="id_trator_ServicoMaquinario")
    implemento = models.ForeignKey(Maquinario,  on_delete=models.CASCADE, related_name="id_implemento_ServicoMaquinario")
    tipo = models.IntegerField('Tipo de Serviço', choices = TIPO_SERVICO_CHOICE)
    data_inicio = models.DateField("Data de Inicio", auto_now = False)
    data_termino = models.DateField("Data de Término", auto_now = False)
    status = models.CharField("Status", max_length= 2, choices = STATUS_CHOICE, default="A")
    observacoes = models.TextField("Observações", max_length = 600, null = True, blank = True)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Prestação de Serviço"
        verbose_name_plural = "Prestação dos Serviços"
        app_label = 'manager'

    def __str__(self):
        return str(self.talhao)

class Plantio(models.Model):
    prestacao_servico = models.ForeignKey(PrestacaoServico, on_delete=models.CASCADE, related_name="id_servico_Plantio")
    quantidade = models.PositiveIntegerField("Quantidade")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Plantio"
        verbose_name_plural = "Plantios"
        app_label = 'manager'

    def __str__(self):
        return str(self.prestacao_servico)

class Fertilizacao(models.Model):
    prestacao_servico = models.ForeignKey(PrestacaoServico, on_delete = models.CASCADE, related_name = "id_servico_Fertilizacao")
    adubo = models.ForeignKey(Adubo, on_delete=models.CASCADE, related_name = "id_adubo_Fertilizacao")
    dosagem = models.FloatField(verbose_name = "Quantidade")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add = True)

    class Meta:
        verbose_name = "Fertilização"
        verbose_name_plural = "Fertilizaçôes"
        app_label = 'manager'

    def __str__(self):
        return str(self.prestacao_servico)

class Colheita(models.Model):
    TIPO_COLHEITA_CHOICE = [
        ("MQ", "Máquina"),
        ("MA", "Mão"),
    ]

    prestacao_servico = models.ForeignKey(PrestacaoServico, on_delete = models.CASCADE, related_name = "id_servico_Colheita")
    data = models.DateField("Data", auto_now = False)
    tipo = models.IntegerField('Tipo de Serviço', choices = TIPO_COLHEITA_CHOICE)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add = True)

    class Meta:
        verbose_name = "Colheita"
        verbose_name_plural = "Colheitas"
        app_label = 'manager'

    def __str__(self):
        return str(self.servico + self.turma_colheita)

class ConsultoriaAgronomo(models.Model):
    agronomo = models.ForeignKey("usuarios.Usuario", on_delete = models.CASCADE, related_name = "id_agronomo_ConsultoriaAgronomo")
    data = models.DateField("Data", auto_now = False)
    fazenda = models.ForeignKey(Fazenda, related_name = "id_fazenda_ConsultoriaAgronomo", on_delete = models.CASCADE)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add = True)

    class Meta:
        verbose_name = "Consultoria do Agrônomo"
        verbose_name_plural = "Consultorias do Agrônomo"
        app_label = 'manager'

    def __str__(self):
        message = f'{self.agronomo.nome} {self.fazenda.nome}'
        return message

class AnotacaoConsultoria(models.Model):
    titulo = models.CharField("Título", max_length = 100)
    consultoria = models.ForeignKey(ConsultoriaAgronomo, related_name="id_consultoria_AnotacaoConsultoria", on_delete=models.CASCADE)
    variedade = models.ForeignKey(Variedade, related_name="id_variedade_AnotacaoConsultoria", on_delete=models.CASCADE)
    litros_cova = models.FloatField("Litros por cova")
    produtividade = models.FloatField("Produtividade por pé")
    produtividade_sacas_hectare = models.FloatField("Produtividade em sacas por hectare")
    descricao = models.TextField("Descricao", max_length=340)
    data_hora_registrado = models.DateTimeField("Horário registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Anotação da Consultoria"
        verbose_name_plural = "Anotações da Consultoria"
        app_label = 'manager'

    def __str__(self):
        return self.titulo

class ArquivoDigitalizado(models.Model):
    descricao = models.CharField("Descricao", max_length = 340)
    # arquivo = models.ForeignKey(ConsultoriaAgronomo, related_name="id_consultoria_AnotacaoConsultoria", on_delete=models.CASCADE)
    data_hora_registrado = models.DateTimeField("Horário registrado", auto_now_add = True)

    class Meta:
        verbose_name = "Anotação da Consultoria"
        verbose_name_plural = "Anotações da Consultoria"
        app_label = 'manager'

    def __str__(self):
        return self.descricao
