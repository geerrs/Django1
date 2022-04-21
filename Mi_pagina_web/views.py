from ast import Return
from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.template import Template , Context
import datetime

def saludo(request):
    return HttpResponse("Hola uwu - Coder")

def segunda_vista(request):
    return HttpResponse("Esta va a ser mi segunda vista")

def diaHoy(request):
    dia = datetime.datetime.now()

    texto= f"Hoy día es {dia}"

    return HttpResponse(texto)

def miNombre(request, nombre):

    texto=f"Mi nombre es {nombre}"

    return HttpResponse(texto)

def edad(self,edad):

    edad2 = int(edad)

    anio = datetime.datetime.today().year

    anio2= int(anio)

    nacimiento = anio2 - edad2

    docDeTex2 = f"Usted nacio en el año {nacimiento}"

    return HttpResponse(docDeTex2)

def probandoTemplate(request):

    miHtml = open("G:\P!2\Mi_pagina_web\Plantillas\pagina1.html")

    plantilla = Template(miHtml.read())

    miHtml.close

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)