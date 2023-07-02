from django.contrib import admin
from .models import Categoria, Producto, Pedido, DetallePedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'precio')
    list_filter = ('categoria',)  # Agrega un filtro por categoría
    search_fields = ('nombre',)  # Agrega una barra de búsqueda por nombre

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id','fecha','mesa','estado']
    list_filter = ['estado']
    inlines = [DetallePedidoInline]

admin.site.site_header = 'Administración del Restaurante'
admin.site.site_title = 'Restaurante Admin'