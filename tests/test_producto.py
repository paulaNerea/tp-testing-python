from producto import Producto
import pytest

def test_actualizar_precio_valido():
    mi_producto = Producto("Yougurt La Serenisima", 1500, "Lacteos")

    mi_producto.actualizar_precio(1000)

    assert mi_producto.precio == 1000
    
   
def test_actualizar_precio_negativo_lanza_error():
    mi_producto = Producto("Yougurt La Serenisima", 1500, "Lacteos")

    with pytest.raises(ValueError) as info_error:
        mi_producto.actualizar_precio(-1000)
    
    assert str(info_error.value) == "El precio no puede ser negativo."

    