from django.contrib import admin

# Register your models here.

from .models import Product, Marca

admin.site.register(Marca)
admin.site.register(Product)