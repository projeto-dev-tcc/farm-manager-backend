from django import forms
from .models import *

class VariedadeForm(forms.ModelForm):
    class Meta:
        model = Variedade
        fields = ('__all__')

        error_messages = {
            "nome":{
                "required": "Por favor, insira o nome é para validar o registro!",
                "invalid": "Por favor, insira um nome válido!",
            }
        }

# class FazendaForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ('__all__')

#         error_messages = {
#             "nome":{
#                 "required": "O nome é obrigatório para o registro!",
#                 "invalid": "Por favor, insira um nome válido!",
#             },
#             "email":{
#                 "required": "O e-mail é obrigatório para o registro!",
#                 "invalid": "Por favor, insira um e-mail válido!",
#             },
#             "sobrenome":{
#                 "required": "O sobrenome é obrigatório para o registro!",
#                 "invalid": "Por favor, insira um sobrenome válido!",
#             },

#             "data_nascimento":{
#                 "required": "A data de nascimento da é obrigatório para o registro!",
#                 "invalid": "Por favor, informe um formato válido para a data de nascimento (DD/DD/AAAA)!",
#             },
#         }