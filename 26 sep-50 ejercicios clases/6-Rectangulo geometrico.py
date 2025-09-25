class retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def cuadrado(self):
        return self.base == self.altura
    
base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

print("El resultado de la operacion es:")
print(f"Area: {retangulo(base, altura).area()}")
print(f"Perimetro: {retangulo(base, altura).perimetro()}")
if retangulo(base, altura).cuadrado():
    print("Es un cuadrado")
else:
    print("No es un cuadrado")