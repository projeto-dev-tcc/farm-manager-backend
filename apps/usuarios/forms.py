from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user

    class Meta:
        model = Usuario
        fields = ('__all__')

        error_messages = {
            "email":{
                "required": "O e-mail é obrigatório para o registro!",
                "invalid": "Por favor, insira um e-mail válido!",
            },
            "nome":{
                "required": "O nome é obrigatório para o registro!",
                "invalid": "Por favor, insira um nome válido!",
            },

            "sobrenome":{
                "required": "O sobrenome é obrigatório para o registro!",
                "invalid": "Por favor, insira um sobrenome válido!",
            },

            "data_nascimento":{
                "required": "A data de nascimento da é obrigatório para o registro!",
                "invalid": "Por favor, informe um formato válido para a data de nascimento (DD/DD/AAAA)!",
            },
        }