from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .carrito import Carrito
from .models import Producto, Categoria

def tienda(request):
    categoria_id = request.GET.getlist('categoria')  # permite seleccionar varias
    productos = Producto.objects.all()
    
    if categoria_id:
        productos = productos.filter(categoria__id__in=categoria_id)

    categorias = Categoria.objects.all()
    carrito = Carrito(request)

    return render(request, 'productos/tienda.html', {
        'productos': productos,
        'categorias': categorias,
        'carrito_total': carrito.contar_items(),
    })

def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = Carrito(request)
    carrito.agregar(producto)
    return redirect('tienda')  # o redirige a 'ver_carrito' si prefieres mostrarlo

def eliminar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = Carrito(request)
    carrito.eliminar(producto)
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = Carrito(request)
    return render(request, 'productos/carrito.html', {
        'carrito': carrito.carrito.items(),  # Usamos items() para acceder a id y datos
        'total': carrito.obtener_total(),
        'carrito_total': carrito.contar_items(),
    })

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = Carrito(request)

    # Buscar productos relacionados (misma categoría, distinto ID)
    relacionados = Producto.objects.filter(categoria=producto.categoria).exclude(id=producto.id)[:4]

    return render(request, 'productos/detalle.html', {
        'producto': producto,
        'relacionados': relacionados,
        'carrito_total': carrito.contar_items(),
    })

def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = Carrito(request)
    cantidad = int(request.POST.get('cantidad', 1))
    carrito.agregar(producto, cantidad)
    return redirect('ver_carrito')
