from dataclasses import fields
from math import prod
from django import forms
from django.forms import ModelForm
from .models import Product

class ProductoForm(ModelForm):
    
    class Meta:
        model = Product
        fields = ['id_producto','marca_producto','nombre_producto',
                    'precio_producto','stock_producto']

