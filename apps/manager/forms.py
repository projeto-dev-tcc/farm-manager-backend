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
        exclude = ["fazenda"]

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
            "data_aquisicao": {
                "required": "Por favor, insira uma data de aquisição para validar o registro!",
                "invalid": "Por favor, insira uma data de aquisição válido!",
            },
        }
        

        widgets = {
            "marca": forms.TextInput(attrs={'placeholder':'Insira a marca...'}),
            "modelo": forms.TextInput(attrs={'placeholder':'Insira o modelo...'}),
            "ano_fabricacao": forms.TextInput(attrs={'placeholder':'Insira o ano de fabricacao...'}),
            "data_aquisicao": forms.TextInput(attrs={'placeholder':'Insira a data de aquisicao...'}),
        }
        
        labels = {
            "tipo": 'Tipo de Maquinário: ',
            "marca": 'Marca: ',
            "modelo": 'Modelo: ',
            "ano_fabricacao": 'Ano de Fabricação: ',
            "data_aquisicao": 'Data de Aquisição: ',
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
            "variedade": forms.TextInput(attrs={'placeholder':'Insira a variedade...'}),
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
        