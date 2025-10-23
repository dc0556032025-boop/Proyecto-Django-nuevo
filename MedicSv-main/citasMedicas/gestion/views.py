from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes})

def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/form.html', {'form': form})

def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')
    return render(request, 'pacientes/form.html', {'form': form})

def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.delete()
    return redirect('lista_pacientes')




