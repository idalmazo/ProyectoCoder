from django import forms

class ClientesFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class ServiciosFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    profesional= forms.CharField(max_length=30)
  
class ProveedoresFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()