from django.shortcuts import render,get_object_or_404
from .models import Tienda
from .models import Producto

# Create your views here.

def tienda_list(request):
  tiendas = Tienda.objects.all()
  return render(request, 'tienda/tienda_list.html', {'tiendas': tiendas})
  

def producto_list(request):
  productos = Producto.objects.all()
  return render(request, 'tienda/producto_list.html', {'prodcutos': productos})