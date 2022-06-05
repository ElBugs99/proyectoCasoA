from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto=models.IntegerField( primary_key=True, verbose_name='Id Producto')
    marca_producto=models.CharField(max_length=20, verbose_name="Marca Producto")
    nombre_producto= models.CharField(max_length=20, null=True, blank=True, verbose_name='Nombre Producto')
    precio_producto= models.IntegerField( verbose_name='Precio Producto')
    stock_producto= models.IntegerField( verbose_name='Stock Producto')
    #categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto



# class Vehiculo(models.Model):
#     patente=models.CharField(max_length=6, primary_key=True, verbose_name='Patente')
#     marca=models.CharField(max_length=20, verbose_name="Marca Vehículo")
#     modelo= models.CharField(max_length=20, null=True, blank=True, verbose_name='Modelo')
#     categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.patente