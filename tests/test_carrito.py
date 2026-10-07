import pytest


def test_calcular_total_carrito(tienda_con_productos):
    carrito = ["Yougurt La Serenisima", "Pan", "Leche"]

    total = tienda_con_productos.calcular_total_carrito(carrito)

    assert total == 4500


def test_calcular_total_carrito_con_un_producto(tienda_con_productos):
    total = tienda_con_productos.calcular_total_carrito(["Pan"])

    assert total == 1000


def test_calcular_total_carrito_vacio(tienda_con_productos):
    total = tienda_con_productos.calcular_total_carrito([])

    assert total == 0


def test_calcular_total_carrito_con_producto_repetido(tienda_con_productos):
    total = tienda_con_productos.calcular_total_carrito(["Pan", "Pan", "Leche"])

    assert total == 4000


def test_calcular_total_carrito_producto_inexistente_lanza_error(tienda_con_productos):
    with pytest.raises(ValueError) as info_error:
        tienda_con_productos.calcular_total_carrito(["Pan", "Gaseosa"])

    assert str(info_error.value) == "No se encontró el producto Gaseosa"


def test_calcular_total_carrito_despues_de_aplicar_descuentos(tienda_con_productos):
    # arrange (Preparar)
    mi_tienda = tienda_con_productos
    carrito = ["Yougurt La Serenisima", "Pan", "Leche"]

    # act (Actuar)
    mi_tienda.aplicar_descuento("Yougurt La Serenisima", 10)
    mi_tienda.aplicar_descuento("Pan", 20)
    total = mi_tienda.calcular_total_carrito(carrito)

    # assert (Verificar)
    assert mi_tienda.buscar_producto("Yougurt La Serenisima").precio == pytest.approx(1350)
    assert mi_tienda.buscar_producto("Pan").precio == pytest.approx(800)
    assert total == pytest.approx(4150)
