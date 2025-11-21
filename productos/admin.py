from django.contrib import admin
from .models import Producto, Detalle, Categoria, Etiqueta

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'categoria')
    list_filter = ('categoria', 'etiquetas')
    search_fields = ('nombre', 'descripcion')
    filter_horizontal = ('etiquetas',)

@admin.register(Detalle)
class DetalleAdmin(admin.ModelAdmin):
    list_display = ('id', 'dimensiones', 'peso')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)