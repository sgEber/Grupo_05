from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido, DetallePedido

def vista_empleado(request):
    mesa = request.GET.get('mesa')
    pedidos = Pedido.objects.all()
    
    if mesa:
        pedidos = pedidos.filter(mesa=mesa)
    
    return render(request, 'empleado/vista_empleado.html', {'pedidos': pedidos})


def cambiar_estado(request, pedido_id):
    if request.method == 'POST':
        estado = request.POST.get('estado')
        pedido = Pedido.objects.get(id=pedido_id)
        pedido.estado = estado
        pedido.save()
        return redirect('vista_empleado')
    
def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    detalles = pedido.detallepedido_set.all()
    return render(request, 'empleado/detalle_pedido.html', {'pedido': pedido, 'detalles': detalles})

