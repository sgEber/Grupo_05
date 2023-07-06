from django.urls import path
from brasas.views import vista_empleado, cambiar_estado, detalle_pedido

urlpatterns = [
    path('empleado/', vista_empleado, name='vista_empleado'),
    
    path('cambiar_estado/<int:pedido_id>/', cambiar_estado, name='cambiar_estado'),
    
    path('detalle_pedido/<int:pedido_id>/', detalle_pedido, name='detalle_pedido'),
]