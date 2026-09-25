from decimal import Decimal, InvalidOperation

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q, Sum
from django.db.models.deletion import ProtectedError
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import (
    Producto,
    Venta,
    DetalleVenta,
)


# ==========================================
# DASHBOARD
# ==========================================

@login_required
def dashboard(request):

    hoy = timezone.localdate()

    productos_total = Producto.objects.count()

    productos_stock_bajo = Producto.objects.filter(
        stock__lte=5
    )

    ventas_hoy = Venta.objects.filter(
        fecha__date=hoy,
        estado="COMPLETADA"
    )

    cantidad_ventas_hoy = ventas_hoy.count()

    total_hoy = ventas_hoy.aggregate(
        total=Sum("total")
    )["total"] or Decimal("0.00")

    ultimas_ventas = Venta.objects.select_related(
        "usuario"
    ).order_by("-fecha")[:5]

    contexto = {
        "productos_total": productos_total,
        "productos_stock_bajo": productos_stock_bajo,
        "cantidad_ventas_hoy": cantidad_ventas_hoy,
        "total_hoy": total_hoy,
        "ultimas_ventas": ultimas_ventas,
    }

    return render(
        request,
        "dashboard.html",
        contexto
    )


# ==========================================
# PRODUCTOS
# ==========================================

@login_required
def index(request):

    productos = Producto.objects.all()

    return render(
        request,
        "productos/index.html",
        {
            "productos": productos
        }
    )


@login_required
@require_POST
def crear(request):

    try:

        codigo_barra = request.POST.get(
            "codigo_barra",
            ""
        ).strip()

        descripcion = request.POST.get(
            "descripcion",
            ""
        ).strip()

        precio_costo = Decimal(
            request.POST.get(
                "precio_costo",
                "0"
            )
        )

        precio_venta = Decimal(
            request.POST.get(
                "precio_venta",
                "0"
            )
        )

        iva = int(
            request.POST.get(
                "iva",
                "10"
            )
        )

        stock = int(
            request.POST.get(
                "stock",
                "0"
            )
        )

        unidad_medida = request.POST.get(
            "unidad_medida",
            "UNIDAD"
        )

        if not codigo_barra:
            raise ValueError(
                "El código de barra es obligatorio."
            )

        if not descripcion:
            raise ValueError(
                "La descripción es obligatoria."
            )

        if precio_costo < 0:
            raise ValueError(
                "El precio de costo no puede ser negativo."
            )

        if precio_venta < 0:
            raise ValueError(
                "El precio de venta no puede ser negativo."
            )

        if stock < 0:
            raise ValueError(
                "El stock no puede ser negativo."
            )

        Producto.objects.create(
            codigo_barra=codigo_barra,
            descripcion=descripcion,
            precio_costo=precio_costo,
            precio_venta=precio_venta,
            iva=iva,
            stock=stock,
            unidad_medida=unidad_medida
        )

        messages.success(
            request,
            "Producto registrado correctamente."
        )

    except (
        ValueError,
        InvalidOperation
    ) as error:

        messages.error(
            request,
            str(error)
        )

    return redirect(
        "productos_index"
    )


@login_required
def editar(request, id):

    producto = get_object_or_404(
        Producto,
        id=id
    )

    if request.method == "POST":

        try:

            producto.codigo_barra = (
                request.POST.get(
                    "codigo_barra",
                    ""
                ).strip()
            )

            producto.descripcion = (
                request.POST.get(
                    "descripcion",
                    ""
                ).strip()
            )

            producto.precio_costo = Decimal(
                request.POST.get(
                    "precio_costo",
                    "0"
                )
            )

            producto.precio_venta = Decimal(
                request.POST.get(
                    "precio_venta",
                    "0"
                )
            )

            producto.iva = int(
                request.POST.get(
                    "iva",
                    "10"
                )
            )

            producto.stock = int(
                request.POST.get(
                    "stock",
                    "0"
                )
            )

            producto.unidad_medida = (
                request.POST.get(
                    "unidad_medida",
                    "UNIDAD"
                )
            )

            if producto.stock < 0:
                raise ValueError(
                    "El stock no puede ser negativo."
                )

            producto.save()

            messages.success(
                request,
                "Producto actualizado correctamente."
            )

            return redirect(
                "productos_index"
            )

        except (
            ValueError,
            InvalidOperation
        ) as error:

            messages.error(
                request,
                str(error)
            )

    return render(
        request,
        "productos/editar.html",
        {
            "producto": producto
        }
    )


@login_required
@require_POST
def eliminar(request, id):

    producto = get_object_or_404(
        Producto,
        id=id
    )

    try:

        producto.delete()

        messages.success(
            request,
            "Producto eliminado correctamente."
        )

    except ProtectedError:

        messages.error(
            request,
            "Este producto ya aparece en una venta y "
            "no puede eliminarse del historial."
        )

    return redirect(
        "productos_index"
    )


# ==========================================
# NUEVA VENTA
# ==========================================

@login_required
def nueva_venta(request):

    if request.method == "POST":

        producto_ids = request.POST.getlist(
            "producto_id"
        )

        cantidades = request.POST.getlist(
            "cantidad"
        )

        try:

            if not producto_ids:
                raise ValueError(
                    "Debe agregar al menos un producto."
                )

            if len(producto_ids) != len(cantidades):
                raise ValueError(
                    "Los datos de la venta son incorrectos."
                )

            cantidades_por_producto = {}

            for producto_id, cantidad_texto in zip(
                producto_ids,
                cantidades
            ):

                producto_id = int(
                    producto_id
                )

                cantidad = int(
                    cantidad_texto
                )

                if cantidad <= 0:

                    raise ValueError(
                        "La cantidad debe ser mayor a cero."
                    )

                cantidades_por_producto[
                    producto_id
                ] = (
                    cantidades_por_producto.get(
                        producto_id,
                        0
                    )
                    + cantidad
                )

            cliente_nombre = (
                request.POST.get(
                    "cliente_nombre",
                    ""
                ).strip()
                or "Consumidor final"
            )

            cliente_ruc = request.POST.get(
                "cliente_ruc",
                ""
            ).strip()

            metodo_pago = request.POST.get(
                "metodo_pago",
                "EFECTIVO"
            )

            if metodo_pago not in [
                "EFECTIVO",
                "TRANSFERENCIA",
                "TARJETA"
            ]:

                raise ValueError(
                    "Método de pago no válido."
                )

            with transaction.atomic():

                venta = Venta.objects.create(
                    cliente_nombre=cliente_nombre,
                    cliente_ruc=cliente_ruc,
                    metodo_pago=metodo_pago,
                    usuario=request.user
                )

                subtotal_general = Decimal(
                    "0.00"
                )

                iva_general = Decimal(
                    "0.00"
                )

                total_general = Decimal(
                    "0.00"
                )

                for producto_id, cantidad in (
                    cantidades_por_producto.items()
                ):

                    producto = (
                        Producto.objects
                        .select_for_update()
                        .get(
                            id=producto_id
                        )
                    )

                    if producto.stock < cantidad:

                        raise ValueError(
                            f"Stock insuficiente para "
                            f"{producto.descripcion}. "
                            f"Disponible: {producto.stock}."
                        )

                    subtotal = (
                        producto.precio_venta
                        * cantidad
                    )

                    iva_monto = (
                        subtotal
                        * Decimal(
                            str(producto.iva)
                        )
                        / Decimal("100")
                    )

                    iva_monto = iva_monto.quantize(
                        Decimal("0.01")
                    )

                    total_linea = (
                        subtotal
                        + iva_monto
                    )

                    DetalleVenta.objects.create(
                        venta=venta,
                        producto=producto,
                        cantidad=cantidad,
                        precio_unitario=(
                            producto.precio_venta
                        ),
                        iva=producto.iva,
                        subtotal=subtotal,
                        iva_monto=iva_monto,
                        total_linea=total_linea
                    )

                    producto.stock -= cantidad

                    producto.save(
                        update_fields=[
                            "stock"
                        ]
                    )

                    subtotal_general += subtotal
                    iva_general += iva_monto
                    total_general += total_linea

                if metodo_pago == "EFECTIVO":

                    monto_pagado = Decimal(
                        request.POST.get(
                            "monto_pagado",
                            "0"
                        )
                    )

                    if monto_pagado < total_general:

                        raise ValueError(
                            "El monto recibido es menor "
                            "al total de la venta."
                        )

                    vuelto = (
                        monto_pagado
                        - total_general
                    )

                else:

                    monto_pagado = (
                        total_general
                    )

                    vuelto = Decimal(
                        "0.00"
                    )

                venta.subtotal = subtotal_general
                venta.iva_total = iva_general
                venta.total = total_general
                venta.monto_pagado = monto_pagado
                venta.vuelto = vuelto

                venta.save()

            messages.success(
                request,
                "Venta registrada correctamente."
            )

            return redirect(
                "factura_venta",
                id=venta.id
            )

        except Producto.DoesNotExist:

            messages.error(
                request,
                "Uno de los productos seleccionados "
                "ya no existe."
            )

        except (
            ValueError,
            InvalidOperation
        ) as error:

            messages.error(
                request,
                str(error)
            )

    productos = Producto.objects.filter(
        stock__gt=0
    ).order_by(
        "descripcion"
    )

    return render(
        request,
        "ventas/nueva.html",
        {
            "productos": productos
        }
    )


# ==========================================
# HISTORIAL DE VENTAS
# ==========================================

@login_required
def lista_ventas(request):

    ventas = Venta.objects.select_related(
        "usuario"
    ).all()

    busqueda = request.GET.get(
        "q",
        ""
    ).strip()

    if busqueda:

        filtro = (
            Q(
                cliente_nombre__icontains=busqueda
            )
            |
            Q(
                cliente_ruc__icontains=busqueda
            )
        )

        if busqueda.isdigit():

            filtro |= Q(
                id=int(busqueda)
            )

        ventas = ventas.filter(
            filtro
        )

    return render(
        request,
        "ventas/lista.html",
        {
            "ventas": ventas,
            "busqueda": busqueda
        }
    )


# ==========================================
# FACTURA
# ==========================================

@login_required
def factura_venta(request, id):

    venta = get_object_or_404(
        Venta.objects.select_related(
            "usuario"
        ).prefetch_related(
            "detalles__producto"
        ),
        id=id
    )

    return render(
        request,
        "ventas/factura.html",
        {
            "venta": venta
        }
    )


# ==========================================
# ANULAR VENTA
# ==========================================

@login_required
@require_POST
def anular_venta(request, id):

    with transaction.atomic():

        venta = get_object_or_404(
            Venta.objects.select_for_update(),
            id=id
        )

        if venta.estado == "ANULADA":

            messages.warning(
                request,
                "Esta venta ya se encuentra anulada."
            )

            return redirect(
                "lista_ventas"
            )

        detalles = venta.detalles.all()

        for detalle in detalles:

            producto = (
                Producto.objects
                .select_for_update()
                .get(
                    id=detalle.producto_id
                )
            )

            producto.stock += detalle.cantidad

            producto.save(
                update_fields=[
                    "stock"
                ]
            )

        venta.estado = "ANULADA"

        venta.save(
            update_fields=[
                "estado"
            ]
        )

    messages.success(
        request,
        "Venta anulada. El stock fue devuelto."
    )

    return redirect(
        "lista_ventas"
    )