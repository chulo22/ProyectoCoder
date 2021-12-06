from django import forms

class FormularioUsuarios(forms.Form):
    nombre= forms.CharField()
    apellido=forms.CharField()
    dni=forms.IntegerField()

class FormularioTurno(forms.Form):
    nombre= forms.CharField()
    actividad=forms.CharField()
    fecha=forms.DateTimeField()