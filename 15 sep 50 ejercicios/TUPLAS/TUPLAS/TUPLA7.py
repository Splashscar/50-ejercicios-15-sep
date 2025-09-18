class Punto3D:
    def __init__(self, x, y, z):
        self.coordenadas = (x, y, z)

    def mostrar(self):
        print(f"Coordenadas 3D: {self.coordenadas}")

p = Punto3D(1, 2, 3)
p.mostrar()
