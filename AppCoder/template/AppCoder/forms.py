from django import forms


class argentinoformulario(forms.Form):
    argentino = forms.CharField(max_length=40)
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()

class extranjeroformulario(forms.Form):
    extranjero = forms.CharField(max_length=40)
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()

class nacionalizadoformulario(forms.Form):
    nacionalizado = forms.CharField(max_length=40)
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    
