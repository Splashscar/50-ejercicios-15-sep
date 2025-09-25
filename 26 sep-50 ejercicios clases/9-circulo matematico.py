class circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * (self.radio ** 2)

    def circunferencia(self):
        return 2 * 3.1416 * self.radio
    def comparar(self, otro_circulo):
        if self.radio > otro_circulo.radio:
            return "El primer círculo es más grande."
        elif self.radio < otro_circulo.radio:
            return "El segundo círculo es más grande."
        else:
            return "Ambos círculos son del mismo tamaño."
        
radio1 = float(input("Ingrese el radio del primer círculo: "))
radio2 = float(input("Ingrese el radio del segundo círculo: "))

circulo1 = circulo(radio1)
circulo2 = circulo(radio2)

print("El resultado de la operacion es:")
print(f"Área del primer círculo: {circulo1.area()}")
print(f"Circunferencia del primer círculo: {circulo1.circunferencia()}")
print(f"Área del segundo círculo: {circulo2.area()}")
print(f"Circunferencia del segundo círculo: {circulo2.circunferencia()}")
print(circulo1.comparar(circulo2))