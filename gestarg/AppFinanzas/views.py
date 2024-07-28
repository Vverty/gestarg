from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Gasto, Ingreso
from .forms import GastoForm, IngresoForm

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
    query = request.GET.get('q')
    if query:
        gastos = Gasto.objects.filter(descripcion__icontains=query)
    else:
        gastos = Gasto.objects.all()
    return render(request, 'AppFinanzas/mostrar_gastos.html', {'gastos': gastos, 'query': query})

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
    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MostrarIngresos')
    else:
        form = IngresoForm()
    return render(request, 'AppFinanzas/agregar_ingreso.html', {'form': form})

def mostrar_ingresos(request):
    query = request.GET.get('q')
    if query:
        ingresos = Ingreso.objects.filter(descripcion__icontains=query)
    else:
        ingresos = Ingreso.objects.all()
    return render(request, 'AppFinanzas/mostrar_ingresos.html', {'ingresos': ingresos, 'query': query})

def editar_ingreso(request, pk):
    ingreso = get_object_or_404(Ingreso, pk=pk)
    if request.method == 'POST':
        form = IngresoForm(request.POST, instance=ingreso)
        if form.is_valid():
            form.save()
            return redirect('MostrarIngresos')
    else:
        form = IngresoForm(instance=ingreso)
    return render(request, 'AppFinanzas/editar_ingreso.html', {'form': form})

def eliminar_ingreso(request, pk):
    ingreso = get_object_or_404(Ingreso, pk=pk)
    if request.method == 'POST':
        ingreso.delete()
        return redirect('MostrarIngresos')
    return render(request, 'AppFinanzas/eliminar_ingreso.html', {'ingreso': ingreso})


