class cuenta_bancaria:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

class cuenta_ahorros(cuenta_bancaria):
    def __init__(self, titular, cantidad=0, tasa_interes=0.02):
        super().__init__(titular, cantidad)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        interes = self.cantidad * self.tasa_interes
        self.cantidad += interes
        return f"Interés aplicado: ${interes:.2f}. Nuevo saldo: ${self.cantidad:.2f}"
    
class cuenta_corriente(cuenta_bancaria):
    def __init__(self, titular, cantidad=0, limite_descubierto=500):
        super().__init__(titular, cantidad)
        self.limite_descubierto = limite_descubierto

    def retirar(self, monto):
        if self.cantidad - monto < -self.limite_descubierto:
            return "Retiro excede el límite de descubierto."
        else:
            self.cantidad -= monto
            return f"Retiro exitoso: ${monto:.2f}. Nuevo saldo: ${self.cantidad:.2f}"
        
