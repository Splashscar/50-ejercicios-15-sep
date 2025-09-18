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

calc.sumar(5, 3)
calc.restar(10, 4)
calc.multiplicar(6, 7)
calc.dividir(8, 2)
calc.dividir(5, 0)

print("Resultados de operaciones:")
for r in calc.resultados:
    print(r)