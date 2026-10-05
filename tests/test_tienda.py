from tienda import Tienda
from producto import Producto

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

def test_buscar_producto_no_existente():
    mi_tienda = Tienda()

    mi_producto = Producto("Yougurt La Serenisima", 1500, "Lacteos")

    resultado = mi_tienda.buscar_producto(mi_producto.nombre)

    assert resultado is None    

def test_eliminar_producto():
    mi_tienda = Tienda()
    mi_producto = Producto("Yougurt La Serenisima", 1500, "Lacteos")
    mi_tienda.agregar_producto(mi_producto)

    mi_tienda.eliminar_producto(mi_producto.nombre)

    assert len(mi_tienda.inventario) == 0
    assert mi_producto not in mi_tienda.inventario