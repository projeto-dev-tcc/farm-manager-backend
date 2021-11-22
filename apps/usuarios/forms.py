from django import forms
from django.forms import widgets
from django.contrib.auth.models import Group
from .models import *

class UsuarioForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length = 30, 
        required = True, 
        label = "Confirmação: ",
        error_messages = {
            "required": "A confirmação de senha é obrigatória para realizar o registro!",
            "invalid": "Por favor, insira uma confirmação de senha válida!",
        },
        widget = forms.TextInput(attrs={'placeholder':'Insira a confirmação de senha...'}),
    )
    
    def save(self, commit=True):
        group = Group.objects.get(name = "Cliente")
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
            user.groups.add(group)
        return user

    class Meta:
        model = Usuario
        fields = ['email', 'nome', "sobrenome", "telefone", "data_nascimento", "password", "confirm_password"]
    
        error_messages = {
            "email":{
                "required": "O e-mail é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um e-mail válido!",
            },
            "nome":{
                "required": "O nome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um nome válido!",
            },

            "sobrenome":{
                "required": "O sobrenome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um sobrenome válido!",
            },
            
            "telefone":{
                "required": "O celular é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um celular válido!",
            },
            
            "password":{
                "required": "A senha é obrigatória para realizar o registro!",
                "invalid": "Por favor, insira uma senha válida!",
            },
            
            "data_nascimento":{
                "invalid": "Por favor, insira um formato válido de data de nascimento (DD/MM/AAAA)!",
            },
        }
        
        widgets = {
            "email": forms.TextInput(attrs={'placeholder':'Insira o e-mail...'}),
            "nome": forms.TextInput(attrs={'placeholder':'Insira o nome...'}),
            "sobrenome": forms.TextInput(attrs={'placeholder':'Insira o sobrenome...'}),
            "telefone": forms.TextInput(attrs={'placeholder':'Insira o celular...'}),
            "data_nascimento": forms.TextInput(attrs={'placeholder':'Insira a data de nascimento...'}),
            "password": forms.TextInput(attrs={'placeholder':'Insira a senha...'}),
        }
        
        labels = {
            "email": 'E-mail: ',
            "nome": 'Nome: ',
            "sobrenome": 'Sobrenome: ',
            "telefone": 'Celular: ',
            "data_nascimento": 'Data de Nascimento: ',
            "password": 'Senha: ',
        }