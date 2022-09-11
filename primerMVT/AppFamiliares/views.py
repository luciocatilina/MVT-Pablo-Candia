from django.shortcuts import render
from AppFamiliares.models import Familiar
from django.http import HttpResponse
from django.template import Template, Context
# Create your views here.

def familiares(request):
    
    familiar1= Familiar(nombre='Ernesto', fechaNacimiento='1980-5-2', numeroTelefonico=1122334455)
    familiar2= Familiar(nombre='Jorge', fechaNacimiento='1990-6-20', numeroTelefonico=1133445566)
    familiar3= Familiar(nombre='Larry', fechaNacimiento='2000-7-26', numeroTelefonico=1144556677)

    familiar1.save()
    familiar2.save()
    familiar3.save()

    diccionario={'nombre1':familiar1.nombre, 'fecha1':familiar1.fechaNacimiento, 'numero1':familiar1.numeroTelefonico,
        'nombre2':familiar2.nombre, 'fecha2':familiar2.fechaNacimiento, 'numero2':familiar2.numeroTelefonico,
        'nombre3':familiar3.nombre, 'fecha3':familiar3.fechaNacimiento, 'numero3':familiar3.numeroTelefonico,
    }

    miHtml=open(r'C:\Users\tu vieja\Desktop\VisualStudioCode\primerMVT\primerMVT\AppFamiliares\plantillaApp\templateApp1.html')

    plantilla=Template(miHtml.read())
    
    miHtml.close()

    miContexto= Context(diccionario)

    documento= plantilla.render(miContexto)

    return HttpResponse(documento)