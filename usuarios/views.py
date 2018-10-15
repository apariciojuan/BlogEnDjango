from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from usuarios.forms import RegistroForm

def register(request):
    if request.method == 'POST':
        f = RegistroForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Cuenta creada, ya puedo hacer Login')
            return redirect('/accounts/registrar/')
    else:
        f = RegistroForm()
    return render(request, 'usuarios/registrar.html', {'form': f})
