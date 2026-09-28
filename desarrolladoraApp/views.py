import json
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from desarrolladoraApp.models import desarrolladora
# Create your views here.
def productos(request):
    return HttpResponse("<h1>Este es el producto de esta distribuidora</h1>")

def ahora(request):
    fecha = datetime.datetime.now()
    salida = f"Desde la distribudora esta en la fecha <b>{fecha}</b>"
    return HttpResponse(salida)

def inicio(request):

    with open('juego.json', 'r', encoding='utf-8') as archivo:
        data = json.load(archivo)

    return render(request, 'desarrolladora/inicio.html', {
        'juego': data[0]
    })
def mostar_desarrolladoras(request):
    data={
        'desarrolladoras': desarrolladora.objects.all()
    }
    return render(request, 'desarrolladora/desarrolladoras.html', data)