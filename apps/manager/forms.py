from django import forms
from .models import *

class VariedadeForm(forms.ModelForm):
    class Meta:
        model = Variedade
        fields = ('__all__')

        error_messages = {
            "nome":{
                "required": "O nome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um nome válido!",
            },
        }
        
        widgets = {
            "nome": forms.TextInput(attrs={'placeholder':'Insira o nome...'}),
        }
        
        labels = {
            "nome": 'Nome: ',
        }

class FazendaForm(forms.ModelForm):
    class Meta:
        model = Fazenda
        fields = ('__all__')
        exclude = ["proprietario"]

        error_messages = {
            "nome":{
                "required": "Por favor, insira um nome para validar o registro!",
                "invalid": "Por favor, insira um nome válido!",
            }
        }
        
        widgets = {
            "nome": forms.TextInput(attrs={'placeholder':'Insira o nome...'}),
        }
        
        labels = {
            "nome": 'Nome: ',
        }

class MaquinarioForm(forms.ModelForm):
    class Meta:
        model = Maquinario
        fields = ('__all__')
        exclude = ["fazenda", "tipo"]

        error_messages = {
            "tipo": {
                "required": "Por favor, insira um tipo para validar o registro!",
                "invalid": "Por favor, insira um tipo válido!",
            },
            "marca": {
                "required": "Por favor, insira uma marca para validar o registro!",
                "invalid": "Por favor, insira uma marca válido!",
            },
            "modelo": {
                "required": "Por favor, insira um modelo para validar o registro!",
                "invalid": "Por favor, insira um modelo válido!",
            },
            "ano_fabricacao": {
                "required": "Por favor, insira um ano de fabricacao para validar o registro!",
                "invalid": "Por favor, insira um ano de fabricacao válido!",
            },
        }
        

        widgets = {
            "marca": forms.TextInput(attrs={'placeholder':'Insira a marca...'}),
            "modelo": forms.TextInput(attrs={'placeholder':'Insira o modelo...'}),
            "ano_fabricacao": forms.TextInput(attrs={'placeholder':'Insira o ano de fabricacao...'}),
        }
        
        labels = {
            "tipo": 'Tipo de Maquinário: ',
            "marca": 'Marca: ',
            "modelo": 'Modelo: ',
            "ano_fabricacao": 'Ano de Fabricação: ',
        }
        
class TalhaoForm(forms.ModelForm):
    class Meta:
        model = Talhao
        fields = ('__all__')
        exclude = ["fazenda"]

        error_messages = {
            "variedade":{
                "required": "A variedade é obrigatória para realizar o registro!",
                "invalid": "Por favor, insira uma variedade válida!",
            },
            
            "nome":{
                "required": "O nome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um nome válido!",
            },
        }
        
        widgets = {
            "nome": forms.TextInput(attrs={'placeholder':'Insira o nome...'}),
            "ano_plantio": forms.TextInput(attrs={'placeholder':'Insira o ano do plantio...'}),
            "numero_covas": forms.TextInput(attrs={'placeholder':'Insira o numero de covas...'}),
            "espacamento_rua": forms.TextInput(attrs={'placeholder':'Insira o espacamento das ruas...'}),
            "espacamento_cova": forms.TextInput(attrs={'placeholder':'Insira o espacamento das covas...'}),
            "area": forms.TextInput(attrs={'placeholder':'Insira a área em hectare...'}),
            "numero_covas_hectare": forms.TextInput(attrs={'placeholder':'Insira o numero de covas por hectare...'}),
        }
        
        labels = {
            "nome": 'Nome: ',
            "variedade": 'Variedade: ',
            "ano_plantio": 'Ano do Plantio: ',
            "numero_covas": 'Número de Covas: ',
            "espacamento_rua": 'Espaçamento das Ruas: ',
            "espacamento_cova": 'Espaçamento das Covas: ',
            "area": 'Área em hectare: ',
            "numero_covas_hectare": 'Número de Covas por Hectare: ',
        }
        
class FuncionarioFazendaForm(forms.ModelForm):
    class Meta:
        model = FuncionarioFazenda
        fields = ('__all__')
        exclude = ["fazenda"]

        error_messages = {
            "funcionario":{
                "required": "O funcionário é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um funcionario válido!",
            },
            
            "tipo":{
                "required": "O tipo é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um tipo válido!",
            },
        }
        
        labels = {
            "funcionario": 'Funcionário: ',
            "tipo": 'Tipo: ',
        }

class AduboForm(forms.ModelForm):
    class Meta:
        model = Adubo
        fields = ('__all__')

        error_messages = {
            "nome":{
                "required": "O nome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um nome válido!",
            },
        }
        
        widgets = {
            "nome": forms.TextInput(attrs={'placeholder':'Insira o nome...'}),
        }
        
        labels = {
            "nome": 'Nome: ',
        }
       
class ConsultoriaAgronomoForm(forms.ModelForm):
    class Meta:
        model = ConsultoriaAgronomo
        fields = ('__all__')
        exclude = ["agronomo", "fazenda", "anotacao_consultoria"]

        error_messages = {
            "data": {
                "required": "Por favor, insira uma  para validar o registro!",
                "invalid": "Por favor, insira uma data válida!",
            },
        }
        
        widgets = {
            "data": forms.TextInput(attrs={'placeholder':'Insira a data...'}),
        }
        
        labels = {
            "data": 'Data: ',
        }
         
class AnotacaoConsultoriaForm(forms.ModelForm):
        class Meta:
            model = AnotacaoConsultoria
            fields = ('__all__')
            exclude = ['consultoria']

            error_messages = {
                "titulo": {
                    "required": "Por favor, insira um título para validar o registro!",
                    "invalid": "Por favor, insira um título válida!",
                },
                "descricao": {
                    "required": "Por favor, insira uma descricao para validar o registro!",
                    "invalid": "Por favor, insira uma descricao válida!",
                },
                "variedade": {
                    "required": "Por favor, insira uma variedade para validar o registro!",
                    "invalid": "Por favor, insira uma variedade válida!",
                },
                "litros_cova": {
                    "required": "Por favor, insira os litros por cova para validar o registro!",
                    "invalid": "Por favor, insira os litros por cova válido!",
                },
                "produtividade": {
                    "required": "Por favor, insira a produtividade para validar o registro!",
                    "invalid": "Por favor, insira uma produtividade válida!",
                },
                "produtividade_sacas_hectare": {
                    "required": "Por favor, insira a produtividade de sacas por hectare para validar o registro!",
                    "invalid": "Por favor, insira uma produtividade de sacas por hectare válida!",
                },
            }
            
            widgets = {
                "titulo": forms.TextInput(attrs={'placeholder':'Insira o título...'}),
                "descricao": forms.TextInput(attrs={'placeholder':'Insira a descricao...'}),
                "litros_cova": forms.TextInput(attrs={'placeholder':'Insira os litros por Cova...'}),
                "produtividade": forms.TextInput(attrs={'placeholder':'Insira a produtividade...'}),
                "produtividade_sacas_hectare": forms.TextInput(attrs={'placeholder':'Insira a produtividade de sacas por hectare...'}),
            }
            
            labels = {
                "titulo": 'Título: ',
                "descricao": 'Descricao: ',
                "variedade": 'Variedade: ',
                "litros_cova": 'Litros por Cova: ',
                "produtividade": 'Produtividade: ',
                "produtividade_sacas_hectare": 'Produtividade de Sacas por Hectare: ',
            }