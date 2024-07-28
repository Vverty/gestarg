from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Gasto
from .forms import GastoForm

def inicio(request):
    return render(request, 'AppFinanzas/index.html')

#GASTOS
def agregar_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MostrarGastos')
    else:
        form = GastoForm()
    return render(request, 'AppFinanzas/agregar_gasto.html', {'form': form})

def mostrar_gastos(request):
    gastos = Gasto.objects.all()  
    context = {
        'gastos': gastos,  
    }
    return render(request, 'AppFinanzas/mostrar_gastos.html', context)

def editar_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id)
    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('MostrarGastos')
    else:
        form = GastoForm(instance=gasto)
    return render(request, 'AppFinanzas/editar_gasto.html', {'form': form})

def eliminar_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id)
    if request.method == 'POST':
        gasto.delete()
        return redirect('MostrarGastos')
    return render(request, 'AppFinanzas/eliminar_gasto.html', {'gasto': gasto})

#INGRESOS
def agregar_ingreso(request):
    return render(request, 'AppFinanzas/agregar_ingreso.html')

def mostrar_ingresos(request):
    return render(request, 'AppFinanzas/mostrar_ingresos.html')

def editar_ingreso(request):
    return render(request, 'AppFinanzas/editar_ingreso.html')

def eliminar_ingreso(request):
    return render(request, 'AppFinanzas/eliminar_ingreso.html')


