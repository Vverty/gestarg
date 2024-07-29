from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Gasto, Ingreso, Cliente
from .forms import GastoForm, IngresoForm, BuscarClienteForm, ClienteForm
from django.db.models import Sum

def inicio(request):
    total_ingresos = Ingreso.objects.aggregate(Sum('monto'))['monto__sum'] or 0
    total_gastos = Gasto.objects.aggregate(Sum('monto'))['monto__sum'] or 0
    cantidad_clientes = Cliente.objects.count()

    context = {
        'total_ingresos': total_ingresos,
        'total_gastos': total_gastos,
        'cantidad_clientes': cantidad_clientes,
    }
    return render(request, 'AppFinanzas/index.html', context)

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

#CLIENTES

def mostrar_clientes(request):
    form = BuscarClienteForm(request.GET or None)
    clientes = Cliente.objects.all()

    razon_social = request.GET.get('razon_social')
    email = request.GET.get('email')

    if razon_social:
        clientes = clientes.filter(razon_social__icontains=razon_social)
    if email:
        clientes = clientes.filter(email__icontains=email)

    context = {
        'clientes': clientes,
        'form': form,
    }

    return render(request, 'AppFinanzas/mostrar_clientes.html', context)

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MostrarClientes')
    else:
        form = ClienteForm()
    return render(request, 'AppFinanzas/agregar_cliente.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('MostrarClientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'AppFinanzas/editar_cliente.html', {'form': form})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('MostrarClientes')
    return render(request, 'AppFinanzas/eliminar_cliente.html', {'cliente': cliente})

