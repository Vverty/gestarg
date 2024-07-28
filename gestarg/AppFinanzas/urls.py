from django.contrib import admin
from django.urls import path
from AppFinanzas import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('gastos/', views.mostrar_gastos, name='MostrarGastos'),
    path('gastos/agregar/', views.agregar_gasto, name='AgregarGasto'),
    path('gastos/editar/<int:id>/', views.editar_gasto, name='EditarGasto'),
    path('gastos/eliminar/<int:id>/', views.eliminar_gasto, name='EliminarGasto'),
    path('agregar-ingreso/', views.agregar_ingreso, name='AgregarIngreso'),
    path('mostrar-ingresos/', views.mostrar_ingresos, name='MostrarIngresos'),
    path('editar-ingreso/', views.editar_ingreso, name='EditarIngreso'),
    path('eliminar-ingreso/', views.eliminar_ingreso, name='EliminarIngreso')
]