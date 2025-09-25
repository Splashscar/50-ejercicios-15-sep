class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pedidos = []

    def hacer_pedido(self, pedido):
        self.pedidos.append(pedido)
        print(f"{self.nombre} hizo un pedido con ID {pedido.id_pedido}.")


class DetallePedido:
    def __init__(self, producto, cantidad, precio):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

    def subtotal(self):
        return self.cantidad * self.precio


class Pedido:
    def __init__(self, id_pedido, cliente):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.detalles = []
        self.estado = "Pendiente"

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)

    def calcular_total(self):
        return sum(d.subtotal() for d in self.detalles)

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"Pedido {self.id_pedido} ahora está en estado: {self.estado}")

    def mostrar_pedido(self):
        print(f"Pedido {self.id_pedido} - Cliente: {self.cliente.nombre}")
        for d in self.detalles:
            print(f"  {d.producto} x{d.cantidad} - ${d.subtotal()}")
        print("Total:", self.calcular_total())
        print("Estado:", self.estado)


cli1 = Cliente("María")
pedido1 = Pedido(1, cli1)

pedido1.agregar_detalle(DetallePedido("Pizza", 2, 25000))
pedido1.agregar_detalle(DetallePedido("Gaseosa", 1, 5000))

cli1.hacer_pedido(pedido1)

pedido1.mostrar_pedido()

pedido1.cambiar_estado("En preparación")
pedido1.cambiar_estado("En camino")
pedido1.cambiar_estado("Entregado")
