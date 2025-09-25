class calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sumar(self):
        print("El resultado de la suma es:", self.a + self.b)
    def restar(self):
        print("El resultado de la resta es:", self.a - self.b)
    def multiplicar(self):
        print("El resultado de la multiplicacion es:", self.a * self.b)
    def dividir(self):
        if self.b != 0:
            print("El resultado de la division es:", self.a / self.b)
        else:
            print("Error: Division por cero no es permitida.")

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))

print("Seleccione la operacion:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
opcion = input("Ingrese la opcion (1/2/3/4): ")
calc = calculadora(a, b)
if opcion == '1':
    calc.sumar()
elif opcion == '2':
    calc.restar()
elif opcion == '3':
    calc.multiplicar()
elif opcion == '4':
    calc.dividir()