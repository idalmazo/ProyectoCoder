import re
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.template import loader
from AppCoder.forms import ClientesFormulario
from AppCoder.models import Clientes
from AppCoder.forms import ProveedoresFormulario, ServiciosFormulario
from AppCoder.models import Proveedores, Servicios


# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada="16")
    curso.save()
    documentoTexto=f"Curso: {curso.nombre} - Camada: {curso.camada}"
    return HttpResponse (documentoTexto) 

def servicios(request):
    #documento=f"Página profesores"
    #return HttpResponse (documento) 
    return render(request, 'AppCoder/servicios.html')

def clientes(request):
    #documento=f"Página profesores"
    #return HttpResponse (documento) 
    return render(request, 'AppCoder/clientes.html')

def proveedores(request):
    return render(request, 'AppCoder/proveedores.html')
    

def inicio(request):
   # plantilla = loader.get_template("padre.html")
    #documento = plantilla.render()
    #return HttpResponse (documento) 
    return render(request, 'AppCoder/inicio.html')

def clientesFormulario(request):
    # plantilla = loader.get_template("padre.html")
    #documento = plantilla.render()
    #return HttpResponse (documento)
    if request.method == 'POST':
        miFormulario = ClientesFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
                
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        email = informacion['email']
        clientes = Clientes (nombre=nombre, apellido=apellido ,email=email) 
        clientes.save()
        return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario= ClientesFormulario()
    return render(request, 'AppCoder/clientesFormulario.html', {'miFormulario':miFormulario})

def serviciosFormulario(request):
    # plantilla = loader.get_template("padre.html")
    #documento = plantilla.render()
    #return HttpResponse (documento)
    if request.method == 'POST':
        miFormulario = ServiciosFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
                
        rama = informacion['rama']
        profesional = informacion['profesional']
        servicios  = Servicios (rama=rama, profesional=profesional) 
        servicios.save()
        return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario= ServiciosFormulario()
    return render(request, 'AppCoder/serviciosFormulario.html', {'miFormulario':miFormulario})

def proveedoresFormulario(request):
    # plantilla = loader.get_template("padre.html")
    #documento = plantilla.render()
    #return HttpResponse (documento)
    if request.method == 'POST':
        miFormulario = ProveedoresFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
                
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        email = informacion['email']
        proveedores = Proveedores (nombre=nombre, apellido=apellido ,email=email) 
        proveedores.save()
        return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario= ProveedoresFormulario()
    return render(request, 'AppCoder/proveedoresFormulario.html', {'miFormulario':miFormulario})

def busquedaProfesional(request):
    return render(request, 'AppCoder/busquedaProfesional.html')        

def buscar(request):
    #respuesta = ("Estoy buscando el profesional:"), {request.GET.get('Profesional')}
    # request.GET ['profesional']}
    if request.GET ['Profesional']:
        profesional = request.GET['Profesional']
        servicios = Servicios.objects.filter (profesional=profesional)
        return render(request, 'AppCoder/respuesta.html', {"servicios":servicios, 'Profesional':profesional})
    else:
        respuesta = "No se ha ingresado ningún profesional"
        return HttpResponse (respuesta)  