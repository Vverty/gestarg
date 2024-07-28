from django.contrib import admin
from django.urls import path
from AppFinanzas import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('agregar-gasto/', views.agregar_gasto, name='AgregarGasto'),
    path('mostrar-gastos/', views.mostrar_gastos, name='MostrarGastos'),
    path('editar-gasto/', views.editar_gasto, name='EditarGastos'),
    path('eliminar-gasto/', views.eliminar_gasto, name='ElimarGasto'),
    path('agregar-ingreso/', views.agregar_ingreso, name='AgregarIngreso'),
    path('mostrar-ingresos/', views.mostrar_ingresos, name='MostrarIngresos'),
    path('editar-ingreso/', views.editar_ingreso, name='EditarIngresos'),
    path('eliminar-ingreso/', views.eliminar_ingreso, name='ElimarIngreso')
]