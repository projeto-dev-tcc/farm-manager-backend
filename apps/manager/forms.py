from django import forms
from .models import *

class VariedadeForm(forms.ModelForm):
    class Meta:
        model = Variedade
        fields = ('__all__')

        error_messages = {
            "nome":{
                "required": "Por favor, insira um nome para validar o registro!",
                "invalid": "Por favor, insira um nome válido!",
            }
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

class MaquinarioForm(forms.ModelForm):
    class Meta:
        model = Maquinario
        fields = ('__all__')

        # error_messages = {
        #     "nome":{
        #         "required": "Por favor, insira um nome para validar o registro!",
        #         "invalid": "Por favor, insira um nome válido!",
        #     }
        # }