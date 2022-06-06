from django.shortcuts import render
from django.template import loader

from core.models import Producto

# Create your views here.

def index(request):
    productos = Producto.objects.all()
    lista=["Pollo con Papas Fritas", "Pastel de Choclo", "Porortos Granados"]
    hijo=Persona("Alan Brito","2")
    
    datos=({"nombre":"Anita La Huerfanita",
              "comidas": lista,
              "hijo":hijo,
              "productos":productos
              })
    return render(request, 'core/index.html', datos)


#   return render(request,'core/test.html',contexto)

def productos(request):

    return render(request, 'core/productos.html')

def Login(request):

    return render(request, 'core/formularioLogin.html')

def adoptar(request):

    return render(request, 'core/adoptar.html')

def aporte(request):

    return render(request, 'core/Aporte.html')

def form(request):

    return render(request, 'core/form.html')

def formularioRegistro(request):

    return render(request, 'core/formularioRegistro.html')

def recuperarPass(request):

    return render(request, 'core/recuperarPass.html')

def terminos(request):

    return render(request, 'core/terminos.html')

def prueba1(request):

    datos={"nombre": "Fulano"}

    return render(request, 'core/index.html', datos)

class Persona:
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()


def formProducto(request):
    return render(request, 'core/formProducto.html')
