class Punto:
    def __init__(self, x, y):
        self.coordenadas = (x, y)

    def mostrar(self):
        print(f"Coordenadas: {self.coordenadas}")

p = Punto(5, 7)
p.mostrar()
