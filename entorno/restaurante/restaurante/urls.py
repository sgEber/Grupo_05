"""
URL configuration for restaurante project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from brasas.views import vista_empleado, cambiar_estado, detalle_pedido
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('empleado/', vista_empleado, name='vista_empleado'),
    
    path('cambiar_estado/<int:pedido_id>/', cambiar_estado, name='cambiar_estado'),
    
    path('detalle_pedido/<int:pedido_id>/', detalle_pedido, name='detalle_pedido'),

]


