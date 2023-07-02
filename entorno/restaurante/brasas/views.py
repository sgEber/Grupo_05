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
            productosListado = Producto.objects.all()
            categoriaListado=Categoria.objects.all()
            context = {
                "producto":productosListado,
                "categoria":categoriaListado
            }
            return render(request, "gestionProductos.html",context)
        else:
            # El usuario no ha proporcionado credenciales vÃ¡lidas
            pass
    return render(request,'Login.html')

def home(request):
    productosListado = Producto.objects.all()
    categoriaListado=Categoria.objects.all()
    context = {
        "producto":productosListado,
        "categoria":categoriaListado
    }
    return render(request, "gestionProductos.html",context)

def registrarProductos(request):
    categoria_nombre = request.POST["txtcategoria"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["numprecio"]

    
    categoria = Categoria.objects.get(nombre=categoria_nombre)
    producto = Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio, categoria=categoria)
    return redirect('/productos')

def edicionProducto(request, id):
    producto = Producto.objects.get(id = id)
    categoriaListado=Categoria.objects.all()
    ayuda = {
        "producto":producto,
        "categoria":categoriaListado
    }
    return render(request, "edicionProductos.html",ayuda)

def editarProducto(request):
    ids = request.POST["txtcodigo"]
    categoria_nombre = request.POST["txtcategoria"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["numprecio"]

    categoria = Categoria.objects.get(nombre=categoria_nombre)
    producto = Producto.objects.get(id = ids)
    producto.categoria = categoria
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.save()

    return redirect('/productos')

def eliminarProductos(request,id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect('/productos')

def buscarProducto(request):
    if request.method == "POST":
        buscarnombre = request.POST.get('nombre')
        busqueda=Producto.objects.filter(nombre__icontains=buscarnombre)
        return render(request,'buscarProductos.html',{"producto":busqueda})
    else:
        productosListado = Producto.objects.all()
        return render(request, "buscarProductos.html",{"producto":productosListado})

#---------------------------------------------------------------
def categorias(request):
    categoriaListado=Categoria.objects.all() 
    return render(request, "gestionCategorias.html",{"categoria":categoriaListado})

def registrarCategorias(request):
    nombre = request.POST["txtnombre"]

    categoria = Categoria.objects.create(nombre=nombre)
    return redirect('/categorias')

def edicionCategoria(request, id):
    categoria = Categoria.objects.get(id = id)
    return render(request, "edicionCategorias.html",{"categoria":categoria})

def editarCategoria(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]

    categoria = Categoria.objects.get(id = codigo)
    categoria.nombre = nombre
    categoria.save()

    return redirect('/categorias')

def eliminarCategorias(request,id):
    categoria = Categoria.objects.get(id = id)
    categoria.delete()
    return redirect('/categorias')

def buscarCategoria(request):
    if request.method == "POST":
        buscarnombre = request.POST.get('nombre')
        busqueda=Categoria.objects.filter(nombre__icontains=buscarnombre)
        return render(request,'buscarCategorias.html',{"categoria":busqueda})
    else:
        categoriasListado = Categoria.objects.all()
        return render(request, "buscarCategorias.html",{"categoria":categoriasListado})