from django.contrib import admin
from django.urls import path
from AppCoder.views import argentino, extranjero, nacionalizado, inicio, argentinoformulario, extranjeroformulario,nacionalizadoformulario



urlpatterns = [
    path('admin/', admin.site.urls),
    path('argentino/', argentino, name='argentino'), 
    path('extranjero/', extranjero, name='extranjero'),
    path('nacionalizado/', nacionalizado, name='nacionalizado'),
    path('inicio/', name= 'Inicio'),
    path('argentinoformulario/', argentinoformulario, name='argentinoformulario'),
    path('extranjeroformulario/', extranjeroformulario, name= 'extranjeroformulario'),
    path('nacionalizadoformulario/', nacionalizadoformulario, name= 'nacionalizadoformulario'),
    
    ]