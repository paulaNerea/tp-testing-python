from unittest.mock import MagicMock
from producto import Producto
import pytest


def test_agregar_producto(tienda_con_productos):
    # arrange (Preparar)
    mi_tienda = tienda_con_productos
    cantidad_inicial = len(mi_tienda.inventario)
    mi_producto = Producto("Queso", 3000, "Lacteos")

    # act (Actuar)
    mi_tienda.agregar_producto(mi_producto)

    # assert (Verificar)
    assert len(mi_tienda.inventario) == cantidad_inicial + 1
    assert mi_producto in mi_tienda.inventario


def test_buscar_producto_existente(tienda_con_productos, mi_producto):
    mi_tienda = tienda_con_productos

    resultado = mi_tienda.buscar_producto(mi_producto.nombre)

    assert resultado == mi_producto


def test_buscar_producto_no_existente_lanza_error(tienda_con_productos):
    mi_tienda = tienda_con_productos

    with pytest.raises(ValueError) as info_error:
        mi_tienda.buscar_producto("Gaseosa")

    assert str(info_error.value) == "No se encontró el producto Gaseosa"


def test_eliminar_producto(tienda_con_productos, mi_producto):
    mi_tienda = tienda_con_productos
    cantidad_inicial = len(mi_tienda.inventario)

    resultado = mi_tienda.eliminar_producto(mi_producto.nombre)

    assert resultado is True
    assert len(mi_tienda.inventario) == cantidad_inicial - 1
    assert mi_producto not in mi_tienda.inventario


def test_eliminar_producto_no_existente_lanza_error(tienda_con_productos):
    mi_tienda = tienda_con_productos

    with pytest.raises(ValueError) as info_error:
        mi_tienda.eliminar_producto("Gaseosa")

    assert str(info_error.value) == "No se encontró el producto Gaseosa"


def test_aplicar_descuento_con_mock(mi_tienda):
    producto_mock = MagicMock()
    producto_mock.nombre = "Gaseosa"
    producto_mock.precio = 500.0
    mi_tienda.agregar_producto(producto_mock)

    mi_tienda.aplicar_descuento("Gaseosa", 20)

    producto_mock.actualizar_precio.assert_called_once_with(400.0)


def test_buscar_producto_en_tienda_vacia_lanza_error(mi_tienda):
    with pytest.raises(ValueError) as info_error:
        mi_tienda.buscar_producto("Pan")

    assert str(info_error.value) == "No se encontró el producto Pan"


def test_eliminar_producto_en_tienda_vacia_lanza_error(mi_tienda):
    with pytest.raises(ValueError) as info_error:
        mi_tienda.eliminar_producto("Pan")

    assert str(info_error.value) == "No se encontró el producto Pan"


def test_aplicar_descuento_negativo_lanza_error(tienda_con_productos):
    with pytest.raises(ValueError) as info_error:
        tienda_con_productos.aplicar_descuento("Pan", -10)

    assert str(info_error.value) == "El porcentaje de descuento debe estar entre 0 y 100."
    assert tienda_con_productos.buscar_producto("Pan").precio == 1000


def test_aplicar_descuento_mayor_a_cien_lanza_error(tienda_con_productos):
    with pytest.raises(ValueError) as info_error:
        tienda_con_productos.aplicar_descuento("Pan", 110)

    assert str(info_error.value) == "El porcentaje de descuento debe estar entre 0 y 100."
    assert tienda_con_productos.buscar_producto("Pan").precio == 1000


def test_aplicar_descuento_cero(tienda_con_productos):
    resultado = tienda_con_productos.aplicar_descuento("Pan", 0)

    assert resultado == 1000
    assert tienda_con_productos.buscar_producto("Pan").precio == 1000


def test_aplicar_descuento_cien(tienda_con_productos):
    resultado = tienda_con_productos.aplicar_descuento("Pan", 100)

    assert resultado == 0
    assert tienda_con_productos.buscar_producto("Pan").precio == 0


def test_aplicar_descuento_producto_inexistente_lanza_error(tienda_con_productos):
    with pytest.raises(ValueError) as info_error:
        tienda_con_productos.aplicar_descuento("Gaseosa", 20)

    assert str(info_error.value) == "No se encontró el producto Gaseosa"
