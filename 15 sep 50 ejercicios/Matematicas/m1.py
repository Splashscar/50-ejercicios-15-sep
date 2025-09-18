class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: división entre 0"

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

calc = Calculadora(num1, num2)

print("Suma:", calc.sumar())
print("Resta:", calc.restar())
print("Multiplicación:", calc.multiplicar())
print("División:", calc.dividir())