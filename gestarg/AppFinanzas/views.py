from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'AppFinanzas/index.html')

#GASTOS
def agregar_gasto(request):
    return render(request, 'AppFinanzas/agregar_gasto.html')

def mostrar_gastos(request):
    return render(request, 'AppFinanzas/mostrar_gastos.html')

def editar_gasto(request):
    return render(request, 'AppFinanzas/editar_gasto.html')

def eliminar_gasto(request):
    return render(request, 'AppFinanzas/eliminar_gasto.html')

#INGRESOS
def agregar_ingreso(request):
    return render(request, 'AppFinanzas/agregar_ingreso.html')

def mostrar_ingresos(request):
    return render(request, 'AppFinanzas/mostrar_ingresos.html')

def editar_ingreso(request):
    return render(request, 'AppFinanzas/editar_ingreso.html')

def eliminar_ingreso(request):
    return render(request, 'AppFinanzas/eliminar_ingreso.html')


