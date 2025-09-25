class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        self.items.append((producto, cantidad))

    def mostrar_carrito(self):
        print("🛒 Carrito:")
        total = 0
        for prod, cant in self.items:
            subtotal = prod.precio * cant
            total += subtotal
            print(f"{prod.nombre} x{cant} - ${subtotal}")
        print("Total:", total)
        return total


class Orden:
    def __init__(self, usuario, carrito):
        self.usuario = usuario
        self.carrito = carrito
        self.total = carrito.mostrar_carrito()
        self.pagada = False

    def mostrar_orden(self):
        print(f"📦 Orden de {self.usuario.nombre} - Total: ${self.total}")
        print("Estado:", "Pagada ✅" if self.pagada else "Pendiente ❌")


class Pago:
    def __init__(self, metodo):
        self.metodo = metodo

    def procesar_pago(self, orden):
        if orden.pagada:
            print("Esta orden ya fue pagada.")
        else:
            print(f"Procesando pago con {self.metodo} por ${orden.total}...")
            orden.pagada = True
            print("✅ Pago exitoso.")





usuario1 = Usuario("Laura")

p1 = Producto("Laptop", 3000)
p2 = Producto("Mouse", 100)


carrito = Carrito()
carrito.agregar_producto(p1, 1)
carrito.agregar_producto(p2, 2)


orden1 = Orden(usuario1, carrito)
orden1.mostrar_orden()


pago1 = Pago("Tarjeta de crédito")
pago1.procesar_pago(orden1)


orden1.mostrar_orden()


pago2 = Pago("PayPal")
pago2.procesar_pago(orden1)
