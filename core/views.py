from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto, Producto
from .forms import ContactoForms, ProductoForm
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'core/index.html')

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'core/productos.html', data)

def contacto(request):
    data = {
        'form': ContactoForms()
    }
    
    if request.method == 'POST':
        formulario = ContactoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
            
    
    
    return render(request, 'core/Contacto.html', data)

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

def formProducto(request):
    return render(request, 'core/formProducto.html')

def agregarProducto(request):

    datos = {'form': ProductoForm()}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado")
        else:
            datos["form"] = formulario

    return render(request, 'core/producto/agregar.html', datos)

def listarProductos(request):

    productos = Producto.objects.all()

    datos = {
        'productos': productos
    }

    return render(request, 'core/producto/listar.html', datos)

def modificarProducto(request, id):

    producto = get_object_or_404(Producto, id=id)

    datos = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto editado")
            return redirect(to="listarProductos")
        else:
            datos["form"] = formulario

    return render(request, 'core/producto/modificar.html',datos)

def eliminarProducto(request, id):
    producto= get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listarProductos")