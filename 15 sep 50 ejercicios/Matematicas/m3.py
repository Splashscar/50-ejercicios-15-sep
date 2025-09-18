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

for i in range(3):
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("Suma:", calc.sumar(num1, num2))
    print("Resta:", calc.restar(num1, num2))
    print("Multiplicación:", calc.multiplicar(num1, num2))
    print("División:", calc.dividir(num1, num2))
    print("-------------------------")

print("Resultados guardados:")
for r in calc.resultados:
    print(r)