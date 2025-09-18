class Calculadora:
    def __init__(self):
        self.resultados = []

    def sumar(self, a, b):
        res = a + b
        self.resultados.append(f"{a} + {b} = {res}")
        return res

    def restar(self, a, b):
        res = a - b
        self.resultados.append(f"{a} - {b} = {res}")
        return res

    def multiplicar(self, a, b):
        res = a * b
        self.resultados.append(f"{a} * {b} = {res}")
        return res

    def dividir(self, a, b):
        if b != 0:
            res = a / b
            self.resultados.append(f"{a} / {b} = {res}")
            return res
        else:
            self.resultados.append(f"{a} / {b} = Error")
            return "Error: división entre 0"

calc = Calculadora()

while True:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /) o 'salir' para terminar: ")

    if operacion == "salir":
        break
    elif operacion == "+":
        print("Resultado:", calc.sumar(num1, num2))
    elif operacion == "-":
        print("Resultado:", calc.restar(num1, num2))
    elif operacion == "*":
        print("Resultado:", calc.multiplicar(num1, num2))
    elif operacion == "/":
        print("Resultado:", calc.dividir(num1, num2))
    else:
        print("Operación no válida")
    print("-------------------------")

print("Resultados guardados:")
for r in calc.resultados:
    print(r)