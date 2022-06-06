from django.contrib import admin

#from ProyectoCoder.AppCoder.views import clientes
from .models import * 

admin.site.register (Curso)
admin.site.register (Clientes)
admin.site.register (Servicios)
admin.site.register (Proveedores)
# Register your models here.
