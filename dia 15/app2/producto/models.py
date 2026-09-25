from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models


class Producto(models.Model):

    codigo_barra = models.CharField(
        max_length=50
    )

    descripcion = models.CharField(
        max_length=150
    )

    precio_costo = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    precio_venta = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    iva = models.IntegerField(
        default=10
    )

    stock = models.IntegerField(
        default=0
    )

    unidad_medida = models.CharField(
        max_length=30,
        default="UNIDAD"
    )

    def __str__(self):
        return self.descripcion

    @property
    def stock_bajo(self):
        return self.stock <= 5

    class Meta:
        ordering = ["descripcion"]


class Venta(models.Model):

    METODOS_PAGO = [
        ("EFECTIVO", "Efectivo"),
        ("TRANSFERENCIA", "Transferencia"),
        ("TARJETA", "Tarjeta"),
    ]

    ESTADOS = [
        ("COMPLETADA", "Completada"),
        ("ANULADA", "Anulada"),
    ]

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    cliente_nombre = models.CharField(
        max_length=150,
        default="Consumidor final"
    )

    cliente_ruc = models.CharField(
        max_length=30,
        blank=True
    )

    metodo_pago = models.CharField(
        max_length=30,
        choices=METODOS_PAGO,
        default="EFECTIVO"
    )

    subtotal = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=Decimal("0.00")
    )

    iva_total = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=Decimal("0.00")
    )

    total = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=Decimal("0.00")
    )

    monto_pagado = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=Decimal("0.00")
    )

    vuelto = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=Decimal("0.00")
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="COMPLETADA"
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.numero_factura

    @property
    def numero_factura(self):

        if not self.pk:
            return "SIN-NUMERO"

        return f"001-001-{self.pk:07d}"

    class Meta:
        ordering = ["-fecha"]


class DetalleVenta(models.Model):

    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
        related_name="detalles"
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT
    )

    cantidad = models.PositiveIntegerField()

    precio_unitario = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    iva = models.IntegerField(
        default=10
    )

    subtotal = models.DecimalField(
        max_digits=14,
        decimal_places=2
    )

    iva_monto = models.DecimalField(
        max_digits=14,
        decimal_places=2
    )

    total_linea = models.DecimalField(
        max_digits=14,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.producto} x {self.cantidad}"