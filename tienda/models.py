from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Tienda(models.Model):
  id= models.AutoField(primary_key=True)
  nombre=models.CharField(max_length=60,default='nombre')
  descr= models.TextField(default='')
  
  def __str__(self):
            return self.nombre
            
class Cliente(models.Model):
  alias=models.CharField(max_length=60,default='nombre')
  email=models.CharField(max_length=60,default='nombre')
  passwd=models.CharField(max_length=60,default='nombre')
  cel=models.CharField(max_length=20,default='nombre')
  phone=models.CharField(max_length=20,default='nombre')
  
  
  def __str__(self):
    return self.alias
            
class Categoria(models.Model):
 
  nombre=models.CharField(max_length=60,default='nombre')
  descr=models.TextField(default='')
  
  def __str__(self):
    return self.nombre
            
class Direccion(models.Model):
  id_user= models.ForeignKey('auth.User', on_delete=models.CASCADE)
  alias=models.CharField(max_length=60,default='nombre')
  calle=models.CharField(max_length=60,default='nombre')
  ciudad=models.CharField(max_length=60,default='nombre')
  cp=models.CharField(max_length=60,default='nombre')
  pais=models.CharField(max_length=60,default='nombre')
  
  def __str__(self):
    return self.alias
            
class Status_envio(models.Model):
  nombre=models.CharField(max_length=60,default='nombre')
  descr=models.CharField(max_length=60,default='nombre')
  
  def __str__(self):
    return self.nombre
    
class Proveedor(models.Model):
  id_categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
  nombre=models.CharField(max_length=60,default='nombre')
  email=models.CharField(max_length=60,default='nombre')
  url=models.CharField(max_length=60,default='nombre')
  cel=models.CharField(max_length=60,default='nombre')
  phone=models.CharField(max_length=60,default='nombre')
  Pais=models.CharField(max_length=60,default='nombre')
  
  def __str__(self):
    return self.nombre
    
class Producto(models.Model):
  id_categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
  id_proveedor= models.ForeignKey(Proveedor, on_delete=models.CASCADE)
  marca=models.CharField(max_length=60,default='nombre')
  nombre=models.CharField(max_length=60,default='nombre')
  descr=models.CharField(max_length=60,default='nombre')
  imagen=models.CharField(max_length=60,default='nombre')
  precio_venta=models.CharField(max_length=60,default='nombre')
  precio_compra=models.CharField(max_length=60,default='nombre')
  
  def __str__(self):
    return self.nombre
            
class Inventario(models.Model):
   id_producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
   cantidad_stock=models.IntegerField()
   cantidad_comprometida=models.IntegerField()
   
   def __str__(self):
     return self.id_producto.nombre
            
class Pedido(models.Model):
  id_cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
  id_producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
  cantidad=models.IntegerField()
  precio=models.CharField(max_length=60,default='nombre')
  fecha=models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return self.nombre
            

            
