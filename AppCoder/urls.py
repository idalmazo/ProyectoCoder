from mimetypes import init
from django.urls import path
#from AppCoder.views import curso 
#from AppCoder import views  
from AppCoder.views import curso, servicios, clientes, proveedores, inicio, clientesFormulario, serviciosFormulario, proveedoresFormulario, busquedaProfesional, buscar


urlpatterns = [
    path('curso/', curso),
    path('servicios/', servicios, name="Servicios"),
    path('clientes/', clientes, name="Clientes"),
    path('proveedores/', proveedores, name="Proveedores"),
    path('', inicio, name="Inicio"),
    path('clientesFormulario/', clientesFormulario, name="ClientesFormulario"),
    path('proveedoresFormulario/', proveedoresFormulario, name="ProveedoresFormulario"),
    path('serviciosFormulario/', serviciosFormulario, name="ServiciosFormulario"),
    path('busquedaProfesional/', busquedaProfesional, name="BusquedaProfesional"),
    path('buscar/', buscar, name="buscar"),
]
