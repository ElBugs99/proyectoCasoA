from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import Contacto, Producto

class ContactoForms(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ["nombre","correo","tipo_consulta","mensaje","avisos"]

class ProductoForm(forms.ModelForm):
    

    class Meta:
        model = Producto
        fields = '__all__'
        # fields = ["nombre_producto","precio_producto",
        #         "descripcion","stock_producto","marca","imagen"]
        widgets = {
        "fecha_elaboracion": forms.SelectDateWidget()
    }
