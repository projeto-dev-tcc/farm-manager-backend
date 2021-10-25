from django.shortcuts import render, redirect
from .models import *
from .forms import *

def registrar_variedade(request):
    form = VariedadeForm()
    if request.method == "POST":
        form = VariedadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, "manager/variedade/registrar_variedade.html", context)
