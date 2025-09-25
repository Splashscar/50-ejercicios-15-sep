import random
from datetime import datetime

class Accion:
    def __init__(self, simbolo, precio_inicial):
        self.simbolo = simbolo
        self.precio = precio_inicial

    def fluctuar_precio(self):
        cambio = random.uniform(-0.1, 0.1) 
        self.precio = max(1, round(self.precio * (1 + cambio), 2))

    def __str__(self):
        return f"{self.simbolo}: ${self.precio}"


class Transaccion:
    def __init__(self, tipo, accion, cantidad, precio):
        self.tipo = tipo 
        self.accion = accion
        self.cantidad = cantidad
        self.precio = precio
        self.fecha = datetime.now()

    def __str__(self):
        return f"[{self.fecha}] {self.tipo.upper()} {self.cantidad} {self.accion.simbolo} a ${self.precio}"


class Portafolio:
    def __init__(self):
        self.saldo = 10000 
        self.posiciones = {}  
        self.historial = []

    def comprar(self, accion, cantidad):
        costo = accion.precio * cantidad
        if costo > self.saldo:
            print("Fondos insuficientes ❌")
            return
        self.saldo -= costo
        self.posiciones[accion.simbolo] = self.posiciones.get(accion.simbolo, 0) + cantidad
        trans = Transaccion("compra", accion, cantidad, accion.precio)
        self.historial.append(trans)
        print(f"✔️ Compra realizada: {cantidad} {accion.simbolo} a ${accion.precio}")

    def vender(self, accion, cantidad):
        if self.posiciones.get(accion.simbolo, 0) < cantidad:
            print("No tienes suficientes acciones ❌")
            return
        ingreso = accion.precio * cantidad
        self.saldo += ingreso
        self.posiciones[accion.simbolo] -= cantidad
        if self.posiciones[accion.simbolo] == 0:
            del self.posiciones[accion.simbolo]
        trans = Transaccion("venta", accion, cantidad, accion.precio)
        self.historial.append(trans)
        print(f"✔️ Venta realizada: {cantidad} {accion.simbolo} a ${accion.precio}")

    def resumen(self, mercado):
        total = self.saldo
        print("\n📊 --- Resumen del Portafolio ---")
        for simbolo, cantidad in self.posiciones.items():
            precio = mercado.obtener_precio(simbolo)
            valor = precio * cantidad
            total += valor
            print(f"{simbolo}: {cantidad} acciones (Precio actual: ${precio}, Valor: ${valor})")
        print(f"Saldo disponible: ${self.saldo}")
        print(f"Valor total del portafolio: ${round(total, 2)}")
        print("---------------------------------\n")

    def historial_transacciones(self):
        print("\n📝 Historial de Transacciones:")
        for t in self.historial:
            print(t)
        print("---------------------------------\n")


class Mercado:
    def __init__(self):
        self.acciones = {}

    def agregar_accion(self, accion):
        self.acciones[accion.simbolo] = accion

    def fluctuar(self):
        for accion in self.acciones.values():
            accion.fluctuar_precio()

    def mostrar(self):
        print("\n📈 --- Precios del Mercado ---")
        for accion in self.acciones.values():
            print(accion)
        print("---------------------------------\n")

    def obtener_precio(self, simbolo):
        return self.acciones[simbolo].precio


mercado = Mercado()
aapl = Accion("AAPL", 150)
tsla = Accion("TSLA", 200)
msft = Accion("MSFT", 100)

mercado.agregar_accion(aapl)
mercado.agregar_accion(tsla)
mercado.agregar_accion(msft)

portafolio = Portafolio()

mercado.mostrar()

portafolio.comprar(aapl, 20)
portafolio.comprar(tsla, 10)

mercado.fluctuar()
mercado.mostrar()

portafolio.vender(aapl, 5)

portafolio.resumen(mercado)
portafolio.historial_transacciones()
