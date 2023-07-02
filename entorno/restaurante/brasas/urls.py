from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.sign_in),

    path('productos',views.home,name='productos'),
    path('registrarProductos',views.registrarProductos),
    path('edicionProducto/<id>/', views.edicionProducto),
    path('editarProducto', views.editarProducto),
    path('eliminarProductos/<id>',views.eliminarProductos),
    path('buscarProducto', views.buscarProducto, name= 'buscarProducto'),

    path('categorias',views.categorias,name='categorias'),
    path('registrarCategorias',views.registrarCategorias),
    path('edicionCategoria/<id>/', views.edicionCategoria),
    path('editarCategoria', views.editarCategoria),
    path('eliminarCategorias/<id>',views.eliminarCategorias),
    path('buscarCategoria', views.buscarCategoria, name= 'buscarCategoria'),
]