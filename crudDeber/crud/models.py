from django.db import models

# Create your models here.
class Cliente(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	cedula = models.CharField(max_length=10)
	direccion = models.CharField(max_length=200)
	telefono = models.CharField(max_length=10)

	def __str__(self):
		return f'{self.nombre}'

class Producto(models.Model):

	nombre = models.CharField(max_length=100)
	precio = models.FloatField()

	def __str__(self):
		return f'{self.nombre} {self.precio}'

class Orden(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	cantidad = models.IntegerField()
	fecha_orden = models.DateField(auto_now_add=True)
	fecha_entrega = models.DateField(auto_now_add=True)

	def __str__(self):
		return f'{self.cliente} {self.producto}'