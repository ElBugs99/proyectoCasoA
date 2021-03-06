
from django.urls import path
from .views import Login, aporte, formularioRegistro, index, productos, adoptar, form, recuperarPass, terminos, contacto, formProducto, agregarProducto, listarProductos, modificarProducto, eliminarProducto

urlpatterns = [
    path('', index, name="index"),
    path('productos/', productos, name="productos"),
    path('login/', Login, name="Login"),
    path('adoptar/', adoptar, name="adoptar"),
    path('aporte/', aporte, name="aporte"),
    path('form/', form, name="form"),
    path('formRegistro/', formularioRegistro, name="formularioRegistro"),
    path('recuperarPass/', recuperarPass, name="recuperarPass"),
    path('terminos/', terminos, name="terminos"),
    path('contacto/', contacto, name="contacto"),
    path('formProducto/', formProducto, name="formProducto"),
    path('agregarProducto/', agregarProducto, name="agregarProducto"),
    path('listarProductos/', listarProductos, name="listarProductos"),
    path('modificarProducto/<id>/', modificarProducto, name="modificarProducto"),
    path('eliminarProducto/<id>/', eliminarProducto, name="eliminarProducto")
]

#path('formulario.html', formulario)