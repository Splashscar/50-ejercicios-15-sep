class cuentaBanco:
    def __init__(self, saldo_privado):
        self.saldo_privado = saldo_privado
    def depositar(self, monto):
        if monto > 0:
            self.saldo_privado += monto
            print(f"Deposito exitoso. Nuevo saldo: {self.saldo_privado}")
        else:
            print("El monto a depositar debe ser positivo.")
    def retirar(self, monto):
        if 0 < monto <= self.saldo_privado:
            self.saldo_privado -= monto
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo_privado}")
        else:
            print("Fondos insuficientes o monto invalido.")

    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo_privado}")

cuenta = cuentaBanco(1000)
while True:
    print("\nSeleccione una operacion:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")
    opcion = input("Ingrese la opcion (1/2/3/4): ")
    if opcion == '1':
        monto = float(input("Ingrese el monto a depositar: "))
        cuenta.depositar(monto)
    elif opcion == '2':
        monto = float(input("Ingrese el monto a retirar: "))
        cuenta.retirar(monto)
    elif opcion == '3':
        cuenta.consultar_saldo()
    elif opcion == '4':
        print("Gracias por usar el sistema bancario.")
        break
    else:
        print("Opcion invalida. Intente de nuevo.")