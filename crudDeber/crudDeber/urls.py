"""crudDeber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from crud.views import cliente, orden, producto, lista_cliente, actualizar_cliente,eliminar_cliente
from crud.views import lista_orden, actualizar_orden, eliminar_orden
from crud.views import lista_producto, actualizar_producto, eliminar_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cliente, name='cliente'),
    path('orden/', orden, name='orden'),
    path('producto/', producto, name='producto'),

    path('lista-cliente/', lista_cliente, name='lista-cliente'),
    path('actualizar-cliente/<int:id>/', actualizar_cliente, name='actualizar-cliente'),
    path('eliminar-cliente/<int:id>/', eliminar_cliente, name='eliminar-cliente'),

    path('lista-orden/', lista_orden, name='lista-orden'),
    path('actualizar-orden/<int:id>/', actualizar_orden, name='actualizar-orden'),
    path('eliminar-orden/<int:id>/', eliminar_orden, name='eliminar-orden'),
    
    path('lista-producto/',lista_producto, name='lista-producto'),
    path('actualizar-producto/<int:id>/', actualizar_producto, name='actualizar-producto'),
    path('eliminar-producto/<int:id>/', eliminar_producto, name='eliminar-producto'),
]

