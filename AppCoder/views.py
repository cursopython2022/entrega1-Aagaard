from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import argentino
from django.template import loader
from AppCoder.forms import argentinoformulario, extranjeroformulario, nacionalizadoformulario


# Create your views here.


def inicio(self):
    plantilla = loader.get_template('appCoder/inicio.html')    
    documento = plantilla.render()
    return HttpResponse(documento)

def argentino(request):
    return render(request, 'appCoder/argentino.html')

def extranjero(request):
    return render(request, 'appCoder/extranjero.html')

def nacionalizado(request):

    return render(request, 'appCoder/nacionalizado.html')        
    
def argentinoformulario(request):
    if request.method == 'POST':
        miformulario = argentinoformulario (request.POST)
        if miformulario.is_valid():
           informacion = miformulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        dni = informacion['dni']
        argentino = argentino(nombre=nombre, apellido=apellido, dni=dni)
        argentino.save()
        return render(request, 'appCoder/inicio.html')
    else :
        miformulario = argentinoformulario()
    return render(request, 'appCoder/argentinoformulario.html')

def extranjeroformulario(request):
    if request.method == 'POST':
        miformulario = extranjeroformulario(request.POST)
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        dni = informacion['dni']
        extranjero = extranjero(nombre=nombre, apellido=apellido, dni=dni)
        extranjero.save()
        return render(request, 'appCoder/inicio.html')
    else :
        miformulario = extranjeroformulario()
    return render(request, 'appCoder/extranjeroformulario.html')

def nacionalizadoformulario(request):
    if request.method == 'POST':
        miformulario = nacionalizadoformulario(request.POST)
        if miformulario.is_valid():
           informacion = miformulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        dni = informacion['dni']
        nacionalizado = nacionalizado(nombre=nombre, apellido=apellido, dni=dni)
        nacionalizado.save()
        return render(request, 'appCoder/inicio.html')
    else :
        miformulario = nacionalizadoformulario()
    return render(request, 'appCoder/nacionalizadoformulario.html')           