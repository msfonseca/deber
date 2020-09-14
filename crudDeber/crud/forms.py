from django.forms import ModelForm
from .models import Cliente, Producto, Orden

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente
		fields = '__all__' #trae todos los campos de llenar

class OrdenForm(ModelForm):
	class Meta:
		model =  Orden
		fields = '__all__' #trae todos los campos de llenar

class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		fields = '__all__' #trae todos los campos de llenar