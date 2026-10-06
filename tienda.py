from producto import Producto

class Tienda:
    def __init__(self):
        self.inventario = []

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.inventario:
            if producto.nombre == nombre:
                return producto
        raise ValueError(f"No se encontró el producto {nombre}")

    def eliminar_producto(self, nombre):
        for producto in self.inventario:
            if producto.nombre == nombre:
                self.inventario.remove(producto)
                return True
        raise ValueError(f"No se encontró el producto {nombre}")

    def aplicar_descuento(self, nombre_producto, porcentaje):
        if not (0 <= porcentaje <= 100):
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        producto = self.buscar_producto(nombre_producto)

        monto_descuento = producto.precio * (porcentaje / 100)
        nuevo_precio = producto.precio - monto_descuento

        producto.actualizar_precio(nuevo_precio)
        return producto.precio