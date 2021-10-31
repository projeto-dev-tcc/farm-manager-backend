from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
import datetime

def base(request):
    context = {}
    if request.user.is_authenticated:
        url_path = request.path
        list_path = []
        if len(url_path) == 1:
            list_path.append('/')
        else:
            for url in url_path[1:]:
                if url == '/':
                    break
                else:
                    list_path.append(url)
                
        url_active = "".join(list_path)
        
        print(f"\n{url_path}\n")
        
        date = datetime.datetime.now().date()
        context = {
            'year': date.year,
            'url_active': url_active
        }
    return context

class SignUpView(CreateView):
    template_name = 'usuarios/signup/signup.html'
    form_class = UsuarioForm

def perfil(request):
    usuario = request.user
    form = UsuarioForm(instance=usuario)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, "usuarios/profile/perfil.html", context)
