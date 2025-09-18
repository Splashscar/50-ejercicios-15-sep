class Contador:
    def __init__(self):
        self.numero = 0

    def aumentar(self):
        self.numero += 1
        print(f"Número actual: {self.numero}")

contador = Contador()

continuar = "s"
while continuar.lower() == "s":
    contador.aumentar()
    continuar = input("¿Quieres aumentar otra vez? (s/n): ")