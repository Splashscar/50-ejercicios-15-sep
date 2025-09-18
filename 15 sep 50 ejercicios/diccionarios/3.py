class Producto:
    def __init__(self, nombre, codigo, precio):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}, Código: {self.codigo}, Precio: ${self.precio}"

inventario = {}
inventario["A1"] = Producto("Laptop", "A1", 3500)
print(inventario["A1"])
