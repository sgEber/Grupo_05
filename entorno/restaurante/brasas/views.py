from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            ProductoListado = Producto.objects.order_by('id')
            return render(request, 'gestionProductos.html', {"productos":ProductoListado}) 
        else:
            # El usuario no ha proporcionado credenciales vÃ¡lidas
            pass
    return render(request,'Login.html')

def home(request):
    productosListado = Producto.objects.all()
    return render(request, "gestionProductos.html",{"productos":productosListado})

def registrarProductos(request):
    categoria = request.POST["txtcategoria"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["numprecio"]

    producto = Producto.objects.create(categoria=categoria, nombre=nombre, descripcion=descripcion, precio=precio)
    return redirect('/')

def edicionProducto(request, id):
    producto = Producto.objects.get(id = id)
    return render(request, "edicionProductos.html",{"producto":producto})

def editarProducto(request):
    categoria = request.POST["txtcategoria"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["numprecio"]

    producto = Producto.objects.get(id = id)
    producto.categoria = categoria
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.save()

    return redirect('/')

def eliminarProductos(request,id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect('/')

def buscarProducto(request):
    if request.method == "POST":
        buscarnombre = request.POST.get('nombre')
        busqueda=Producto.objects.filter(nombre__icontains=buscarnombre)
        return render(request,'buscarProductos.html',{"producto":busqueda})
    else:
        productosListado = Producto.objects.all()
        return render(request, "buscarProductos.html",{"producto":productosListado})