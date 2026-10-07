import pytest


def test_actualizar_precio_valido(mi_producto):
    mi_producto.actualizar_precio(1000)

    assert mi_producto.precio == 1000


def test_actualizar_precio_negativo_lanza_error(mi_producto):
    with pytest.raises(ValueError) as info_error:
        mi_producto.actualizar_precio(-1000)

    assert str(info_error.value) == "El precio no puede ser negativo."
    assert mi_producto.precio == 1500


def test_actualizar_precio_a_cero(mi_producto):
    mi_producto.actualizar_precio(0)

    assert mi_producto.precio == 0
