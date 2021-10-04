from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.urls import reverse

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Insira um e-mail válido para continuar!')

        usuario = self.model(
            email=self.normalize_email(email),
        )
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False
        if password:
            usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, email,  password, **kwargs):
        usuario = self.create_user(
            email=self.normalize_email(email),
            password=password,
            **kwargs
        )
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.set_password(password)
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name = "E-mail", max_length = 194, unique = True)
    nome = models.CharField(verbose_name = "Nome", max_length = 60)
    sobrenome = models.CharField(verbose_name = "Sobrenome", max_length = 150)
    telefone = models.CharField(verbose_name = "Telefone", max_length = 15)
    data_nascimento = models.DateField(verbose_name = "Data de nascimento", auto_now_add = False, auto_now = False, null = True)

    is_active = models.BooleanField(verbose_name = "Usuário ativo", default = True)
    is_staff = models.BooleanField(verbose_name = "Usuário desenvolvedor", default = False)
    is_superuser = models.BooleanField(verbose_name = "Super usuário", default = False)

    USERNAME_FIELD = "email"

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('index')
        # return reverse('index', args=[str(self.id)]) CASO NECESSITASSE PASSAR ID

class Fazenda(models.Model):
    nome = models.CharField("Nome", max_length=240)
    proprietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="proprietario")
    funcionarios = models.ManyToManyField(Usuario, related_name="funcionarios")
    agronomos = models.ManyToManyField(Usuario, related_name="agronomos")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    def __str__(self):
        return self.nome

class Maquinario(models.Model):
    TIPO_MAQUINARIO_CHOICE = [
        (1, "Trator"),
        (2, "Emplemento")
    ]
    
    fazenda = models.ForeignKey(Fazenda, on_delete=models.CASCADE)
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
    variedade = models.ManyToManyField(Variedade)
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
	

#ARRUMAR DATA DE ÍNICIO E DE TÉRMINO!!!!!!!!!!
class Servico(models.Model):
    TIPO_SERVICO_CHOICE = [
        (1, "Plantio"),
        (2, "Fertilização"),
        (3, "Preparação do Solo"),
        (4, "Outros"),
    ]
    
    talhao = models.ForeignKey(Talhao, on_delete=models.CASCADE)
    maquinario = models.ForeignKey(Maquinario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.IntegerField('Tipo de Serviço', choices=TIPO_SERVICO_CHOICE)
    data_inicio = models.DateField("Data de Inicio")
    data_termino = models.DateField("Data de Término")
    observacoes = models.TextField("Observações")
    data_hora_registrado = models.DateTimeField("Horário Registrado", auto_now_add=True)

    def __str__(self):
        return str(self.tipo + self.talhao)