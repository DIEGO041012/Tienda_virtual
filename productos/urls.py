from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name='tienda'),
]

#carrito
urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('agregar/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('eliminar/<int:producto_id>/', views.eliminar_carrito, name='eliminar_carrito'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),

]


