class dado:
    def __init__(self, caras):
        self.caras = caras

    def lanzar(self):
        import random
        return random.randint(1, self.caras)    
    def estadisticas(self, lanzamientos):
        resultados = [self.lanzar() for _ in range(lanzamientos)]
        frecuencia = {i: resultados.count(i) for i in range(1, self.caras + 1)}
        return frecuencia
    
caras = int(input("Ingrese el número de caras del dado (por ejemplo, 6 para un dado estándar): "))
dado_juego = dado(caras)
lanzamientos = int(input("Ingrese el número de lanzamientos que desea realizar: "))
resultados = dado_juego.estadisticas(lanzamientos)
print(f"Resultados de lanzar un dado de {caras} caras {lanzamientos} veces:")
for cara, frecuencia in resultados.items():
    print(f"Cara {cara}: {frecuencia} veces")
