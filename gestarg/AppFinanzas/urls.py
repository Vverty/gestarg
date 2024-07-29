from django.contrib import admin
from django.urls import path
from AppFinanzas import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('gastos/', views.mostrar_gastos, name='MostrarGastos'),
    path('gastos/agregar/', views.agregar_gasto, name='AgregarGasto'),
    path('gastos/editar/<int:id>/', views.editar_gasto, name='EditarGasto'),
    path('gastos/eliminar/<int:id>/', views.eliminar_gasto, name='EliminarGasto'),
    path('agregar_ingreso/', views.agregar_ingreso, name='AgregarIngreso'),
    path('mostrar_ingresos/', views.mostrar_ingresos, name='MostrarIngresos'),
    path('editar_ingreso/<int:pk>/', views.editar_ingreso, name='EditarIngreso'),
    path('eliminar_ingreso/<int:pk>/', views.eliminar_ingreso, name='EliminarIngreso'),
    path('agregar_cliente/', views.agregar_cliente, name='AgregarCliente'),
    path('mostrar_clientes/', views.mostrar_clientes, name='MostrarClientes'),
    path('editar_cliente/<int:pk>/', views.editar_cliente, name='EditarCliente'),
    path('eliminar_cliente/<int:pk>/', views.eliminar_cliente, name='EliminarCliente'),
]