class Producto:
    def __init__ (self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def descuentos10(self):
        return self.precio * 0.9
    def descuentos20(self):
        return self.precio * 0.8
    
    def actualizar_stock(self, cantidad_vendida):
        if cantidad_vendida <= self.stock:
            self.stock -= cantidad_vendida
            print(f"Stock actualizado. Nuevo stock de {self.nombre}: {self.stock}")
        else:
            print(f"No hay suficiente stock de {self.nombre}. Stock actual: {self.stock}")

producto1 = Producto("Laptop", 1000, 10)
producto2 = Producto("Smartphone", 500, 20)
producto3 = Producto("Tablet", 300, 15)

print(f"Producto: {producto1.nombre}, Precio: {producto1.precio}, Stock: {producto1.stock}")
print(f"Precio con 10% de descuento: {producto1.descuentos10()}")
print(f"Precio con 20% de descuento: {producto1.descuentos20()}")
producto1.actualizar_stock(3)

print(f"Producto: {producto2.nombre}, Precio: {producto2.precio}, Stock: {producto2.stock}")
print(f"Precio con 10% de descuento: {producto2.descuentos10()}")
print(f"Precio con 20% de descuento: {producto2.descuentos20()}")
producto2.actualizar_stock(5)

print(f"Producto: {producto3.nombre}, Precio: {producto3.precio}, Stock: {producto3.stock}")
print(f"Precio con 10% de descuento: {producto3.descuentos10()}")
print(f"Precio con 20% de descuento: {producto3.descuentos20()}")
producto3.actualizar_stock(20)