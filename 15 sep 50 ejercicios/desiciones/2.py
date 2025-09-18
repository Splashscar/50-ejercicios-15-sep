class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_descuento(self):
        if self.precio > 1000:
            return f"El producto {self.nombre} tiene descuento. Precio final: {self.precio * 0.9}"
        else:
            return f"El producto {self.nombre} no tiene descuento. Precio: {self.precio}"


producto = Producto("Laptop", 1500)
print(producto.calcular_descuento())
