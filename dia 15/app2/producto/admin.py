from django.contrib import admin

from .models import (
    Producto,
    Venta,
    DetalleVenta,
)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):

    list_display = (
        "codigo_barra",
        "descripcion",
        "precio_venta",
        "iva",
        "stock",
        "unidad_medida",
    )

    search_fields = (
        "codigo_barra",
        "descripcion",
    )


class DetalleVentaInline(
    admin.TabularInline
):

    model = DetalleVenta

    extra = 0

    readonly_fields = (
        "producto",
        "cantidad",
        "precio_unitario",
        "iva",
        "subtotal",
        "iva_monto",
        "total_linea",
    )


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "fecha",
        "cliente_nombre",
        "metodo_pago",
        "total",
        "estado",
        "usuario",
    )

    list_filter = (
        "estado",
        "metodo_pago",
        "fecha",
    )

    search_fields = (
        "cliente_nombre",
        "cliente_ruc",
    )

    inlines = [
        DetalleVentaInline
    ]