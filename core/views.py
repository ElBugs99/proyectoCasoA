from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'core/index.html')

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
