class Rectangulo:
    def __init__(self, largo, ancho):
        self.dimensiones = (largo, ancho)

    def area(self):
        return self.dimensiones[0] * self.dimensiones[1]

r = Rectangulo(5, 3)
print("Área:", r.area())
