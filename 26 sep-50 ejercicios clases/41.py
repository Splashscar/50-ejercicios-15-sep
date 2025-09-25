from datetime import datetime


class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.transacciones = []
    
    def depositar(self, monto):
        self.saldo += monto
        self.transacciones.append(Transaccion("Depósito", monto))
        print(f"✅ Se depositaron ${monto}. Saldo actual: ${self.saldo}")
    
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            self.transacciones.append(Transaccion("Retiro", monto))
            print(f"💸 Se retiraron ${monto}. Saldo actual: ${self.saldo}")
        else:
            print("❌ Fondos insuficientes.")
    
    def mostrar_historial(self):
        print(f"📒 Historial de {self.titular}:")
        for t in self.transacciones:
            print(t)

class Transaccion:
    def __init__(self, tipo, monto):
        self.tipo = tipo
        self.monto = monto
        self.fecha = datetime.now()
    
    def __str__(self):
        return f"[{self.fecha.strftime('%Y-%m-%d %H:%M')}] {self.tipo}: ${self.monto}"

class Tarjeta:
    def __init__(self, numero, cuenta, limite_credito=1000):
        self.numero = numero
        self.cuenta = cuenta
        self.limite_credito = limite_credito
        self.deuda = 0
    
    def comprar(self, monto):
        if self.deuda + monto <= self.limite_credito:
            self.deuda += monto
            print(f"🛒 Compra de ${monto} realizada. Deuda actual: ${self.deuda}")
        else:
            print("❌ Límite de crédito excedido.")
    
    def pagar(self, monto):
        if monto <= self.cuenta.saldo:
            self.cuenta.retirar(monto)
            self.deuda -= monto
            print(f"✅ Pago de tarjeta por ${monto}. Deuda actual: ${self.deuda}")
        else:
            print("❌ Saldo insuficiente en cuenta.")

class Prestamo:
    def __init__(self, cuenta, monto, interes=0.05):
        self.cuenta = cuenta
        self.monto = monto
        self.interes = interes
        self.deuda = monto + (monto * interes)
        self.pagado = 0
        self.estado = "Activo"
        self.cuenta.depositar(monto)
        print(f"🏦 Préstamo aprobado: ${monto} con interés del {interes*100}%. Deuda total: ${self.deuda}")
    
    def pagar_cuota(self, monto):
        if monto <= self.cuenta.saldo:
            self.cuenta.retirar(monto)
            self.pagado += monto
            self.deuda -= monto
            if self.deuda <= 0:
                self.estado = "Pagado"
                print("🎉 Préstamo totalmente saldado.")
            else:
                print(f"💵 Pago de ${monto}. Deuda restante: ${self.deuda}")
        else:
            print("❌ Saldo insuficiente en cuenta para pagar la cuota.")



cuenta1 = Cuenta("Carlos", 500)

cuenta1.depositar(300)
cuenta1.retirar(200)


tarjeta1 = Tarjeta("1234-5678", cuenta1, 1500)
tarjeta1.comprar(400)
tarjeta1.pagar(200)

prestamo1 = Prestamo(cuenta1, 1000, interes=0.1)
prestamo1.pagar_cuota(500)
prestamo1.pagar_cuota(800)


print("\n--- HISTORIAL FINAL ---")
cuenta1.mostrar_historial()
