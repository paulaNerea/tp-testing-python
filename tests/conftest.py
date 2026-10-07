from producto import Producto
from tienda import Tienda
import pytest


@pytest.fixture
def mi_producto():
    return Producto("Yougurt La Serenisima", 1500, "Lacteos")


@pytest.fixture
def mi_tienda():
    return Tienda()


@pytest.fixture
def tienda_con_productos(mi_tienda, mi_producto):
    mi_tienda.agregar_producto(mi_producto)
    mi_tienda.agregar_producto(Producto("Pan", 1000, "Panaderia"))
    mi_tienda.agregar_producto(Producto("Leche", 2000, "Lacteos"))
    return mi_tienda
