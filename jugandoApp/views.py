
import json
from django.shortcuts import render
from django.http import HttpResponse
from jugandoApp.models import Juego

# Create your views here.
def eljugado (request):
    return render(request, 'jugando/inicio.html')

def inicio(request):
    return render(request, 'main.html')

def listado(request):

    with open('juegos.json', 'r', encoding='utf-8') as archivo:
        juegos = json.load(archivo)

    return render(request, 'jugando/listado.html', {
        'juegos': juegos
    })
def mostar_juegos(request):
    data={
        'juegos': Juego.objects.all()
    }
    return render(request, 'jugando/juegos.html', data)