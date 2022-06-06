from dataclasses import fields
from math import prod
from django import forms
from django.forms import ModelForm
from .models import Producto

class ProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = ['id_producto','marca_producto','nombre_producto',
                    'precio_producto','stock_producto']

