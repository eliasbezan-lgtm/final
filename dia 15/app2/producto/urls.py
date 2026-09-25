from django.urls import path

from . import views


urlpatterns = [

    # DASHBOARD
    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    # PRODUCTOS
    path(
        "productos/",
        views.index,
        name="productos_index"
    ),

    path(
        "productos/crear/",
        views.crear,
        name="productos_crear"
    ),

    path(
        "productos/editar/<int:id>/",
        views.editar,
        name="productos_editar"
    ),

    path(
        "productos/eliminar/<int:id>/",
        views.eliminar,
        name="productos_eliminar"
    ),

    # VENTAS
    path(
        "ventas/",
        views.lista_ventas,
        name="lista_ventas"
    ),

    path(
        "ventas/nueva/",
        views.nueva_venta,
        name="nueva_venta"
    ),

    path(
        "ventas/<int:id>/factura/",
        views.factura_venta,
        name="factura_venta"
    ),

    path(
        "ventas/<int:id>/anular/",
        views.anular_venta,
        name="anular_venta"
    ),
]