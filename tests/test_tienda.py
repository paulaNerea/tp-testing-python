from unittest.mock import MagicMock
from tienda import Tienda
from producto import Producto
import pytest

def test_agregar_producto():
    # arrange (Preparar)
    mi_tienda = Tienda()
    # act (Actuar)
    mi_producto = Producto("Yougurt La Serenisima", 1500, "Lacteos")
    mi_tienda.agregar_producto(mi_producto)
    # assert (Verificar)
    assert len(mi_tienda.inventario) == 1
    assert mi_producto in mi_tienda.inventario

def test_buscar_producto_existente():
    mi_tienda = Tienda()

    mi_producto = Producto("Yougurt La Serenisima", 1500, "Lacteos")
    mi_tienda.agregar_producto(mi_producto)

    resultado = mi_tienda.buscar_producto(mi_producto.nombre)

    assert resultado == mi_producto

def test_buscar_producto_no_existente_lanza_error():
    mi_tienda = Tienda()

    with pytest.raises(ValueError) as info_error:
        mi_tienda.buscar_producto("Yougurt La Serenisima")
    
    assert str(info_error.value) == "No se encontró el producto Yougurt La Serenisima"

def test_eliminar_producto():
    mi_tienda = Tienda()
    mi_producto = Producto("Yougurt La Serenisima", 1500, "Lacteos")
    mi_tienda.agregar_producto(mi_producto)

    mi_tienda.eliminar_producto(mi_producto.nombre)

    assert len(mi_tienda.inventario) == 0
    assert mi_producto not in mi_tienda.inventario

def test_eliminar_producto_no_existente_lanza_error():
    mi_tienda = Tienda()

    with pytest.raises(ValueError) as info_error:
        mi_tienda.eliminar_producto("Yougurt La Serenisima")

    assert str(info_error.value) == "No se encontró el producto Yougurt La Serenisima"

def test_aplicar_descuento_con_mock():
    mi_tienda = Tienda()

    producto_mock = MagicMock()
    producto_mock.nombre = "Gaseosa"
    producto_mock.precio = 500.0  
    mi_tienda.agregar_producto(producto_mock)

    mi_tienda.aplicar_descuento("Gaseosa", 20)

    producto_mock.actualizar_precio.assert_called_once_with(400.0)
    