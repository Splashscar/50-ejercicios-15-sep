class Producto:
    def __init__(self, nombre, precio):
        self.datos = (nombre, precio)

    def mostrar(self):
        print(f"Producto: {self.datos[0]}, Precio: ${self.datos[1]}")

prod = Producto("Lápiz", 1.5)
prod.mostrar()
