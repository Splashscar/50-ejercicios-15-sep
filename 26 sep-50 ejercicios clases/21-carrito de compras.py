class carritoCompras:
    def __init__ (self, producto, precio, cantidad):
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad

class Producto(carritoCompras):
    def __init__(self, producto, precio, cantidad):
        super().__init__(producto, precio, cantidad)

    def descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        precio_final = self.precio - descuento
        return f"El precio final de {self.producto} con un descuento del {porcentaje}% es: ${precio_final:.2f}"
    def total(self):
        total = self.precio * self.cantidad
        return f"El total a pagar por {self.cantidad} unidades de {self.producto} es: ${total:.2f}"
    
producto1 = Producto("Laptop", 1500, 2)
print(producto1.descuento(10))
print(producto1.total())
producto2 = Producto("Smartphone", 800, 3)
print(producto2.descuento(5))
print(producto2.total())
