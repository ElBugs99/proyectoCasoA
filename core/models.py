from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre =models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre

class Product(models.Model):
    id_producto=models.IntegerField( primary_key=True, verbose_name='Id')
    nombre_producto= models.CharField(max_length=20, null=True, blank=True, verbose_name='Nombre Producto')
    precio_producto= models.IntegerField( verbose_name='Precio Producto')
    descripcion= models.TextField(max_length=50, null=True, verbose_name='Descripcion Producto')
    stock_producto= models.IntegerField( verbose_name='Stock Producto')
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    #categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        #toString
        return self.nombre_producto



# class Vehiculo(models.Model):
#     patente=models.CharField(max_length=6, primary_key=True, verbose_name='Patente')
#     marca=models.CharField(max_length=20, verbose_name="Marca Vehículo")
#     modelo= models.CharField(max_length=20, null=True, blank=True, verbose_name='Modelo')
#     categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.patente