from django.db import models

class Fazenda(models.Model):
    nome = models.CharField("Nome", max_length=240)
    proprietario = models.ForeignKey("usuarios.Usuario", related_name="id_proprietario_Fazenda", on_delete=models.CASCADE)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

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

    def __str__(self):
        return self.nome

class Maquinario(models.Model):
    TIPO_MAQUINARIO_CHOICE = [
        (1, "Trator"),
        (2, "Emplemento")
    ]

    fazenda = models.ForeignKey(Fazenda, related_name="id_fazenda_Maquinario", on_delete=models.CASCADE)
    tipo = models.IntegerField('Tipo de Maquinário', choices=TIPO_MAQUINARIO_CHOICE)
    marca = models.CharField("Marca", max_length=200)
    modelo = models.CharField("Modelo", max_length=200)
    ano_fabricacao = models.CharField("Ano", max_length=240)
    horas_trabalhadas = models.PositiveIntegerField("Horas Trabalhadas")
    data_aquisicao = models.DateField("Data de Aquisição", auto_now_add=True)
    observacoes = models.TextField("Observações")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    def __str__(self):
        return str(self.marca + self.modelo + self.ano)

class Variedade(models.Model):
    nome = models.CharField("Nome", max_length=240)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    def __str__(self):
        return self.nome

class Talhao(models.Model):
    variedade = models.ManyToManyField(Variedade, related_name="id_variedade_Talhao")
    nome = models.CharField("Nome", max_length=200)
    ano_plantio = models.CharField("Ano do plantio", max_length=10, blank=True, null=True)
    numero_covas = models.PositiveIntegerField("Numero de covas", blank=True, null=True)
    espacamento_rua = models.FloatField("Espaçamento das ruas", blank=True, null=True)
    espacamento_cova = models.FloatField("Espaçamento das covas", blank=True, null=True)
    area = models.FloatField("Área em hectare", blank=True, null=True)
    numero_covas_hectare = models.PositiveIntegerField("Número de covas por hectare", blank=True, null=True)
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    def __str__(self):
        return str(self.nome)

class Servico(models.Model):
    TIPO_SERVICO_CHOICE = [
        (1, "Plantio"),
        (2, "Fertilização"),
        (3, "Preparação do Solo"),
        (4, "Outros"),
    ]
    
    talhao = models.ForeignKey(Talhao, on_delete=models.CASCADE, related_name="id_talhao_Servico")
    maquinario = models.ForeignKey(Maquinario, on_delete=models.CASCADE, related_name="id_maquinario_Servico")
    usuario = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE, related_name="id_usuario_Servico")
    tipo = models.IntegerField('Tipo de Serviço', choices=TIPO_SERVICO_CHOICE)
    data_inicio = models.DateField("Data de Inicio", auto_now = False)
    data_termino = models.DateField("Data de Término", auto_now = False)
    observacoes = models.TextField("Observações")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    def __str__(self):
        return str(self.tipo + self.talhao)
