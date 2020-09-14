from django.shortcuts import render, redirect
from .forms import ClienteForm, OrdenForm, ProductoForm
from .models import Cliente
from .models import Orden
from .models import Producto
# Create your views here.

def cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista-cliente')
    else:
        form = ClienteForm()
    return render(request, 'crear/cliente.html', {'form': form})


def orden(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista-orden')
    else:
        form = OrdenForm()
    return render(request, 'crear/orden.html', {'form': form})

def producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductoForm()
    return render(request, 'crear/producto.html', {'form': form})
#################################################################################################

def lista_cliente(request):
    lista = Cliente.objects.all()
    contexto = {'clientes': lista}
    return render(request, 'lista/cliente.html', contexto)

def actualizar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
        return redirect('lista-cliente')
    return render(request, 'actualizar/cliente.html',{'form':form})

def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista-cliente')

    return render(request, 'eliminar/cliente.html',{'clientes':cliente})


    #################################################################################################

def lista_orden(request):

    lista = Orden.objects.all()
    contexto = {'orden': lista}

    return render(request, 'lista/orden.html', contexto)

def actualizar_orden(request, id):
    orden = Orden.objects.get(id=id)
    if request.method == 'GET':
        form = OrdenForm(instance=orden)
    else:
        form = OrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
        return redirect('lista-orden')
    return render(request, 'actualizar/orden.html',{'form':form})

def eliminar_orden(request, id):
    orden = Orden.objects.get(id=id)
    if request.method == 'POST':
        orden.delete()
        return redirect('lista-orden')

    return render(request, 'eliminar/orden.html',{'orden':orden})

        #################################################################################################

def lista_producto(request):
    lista = Producto.objects.all()
    contexto = {'productos': lista}
    return render(request, 'lista/producto.html', contexto)

def actualizar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('lista-producto')
    return render(request, 'actualizar/producto.html',{'form':form})

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista-producto')

    return render(request, 'eliminar/producto.html',{'productos':producto})
