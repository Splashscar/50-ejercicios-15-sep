class Luz:
    def __init__(self):
        self.estado = "apagada"

    def cambiar(self):
        if self.estado == "apagada":
            self.estado = "encendida"
        else:
            self.estado = "apagada"
        print(f"La luz está {self.estado}")

luz = Luz()

continuar = "s"
while continuar.lower() == "s":
    luz.cambiar()
    continuar = input("¿Quieres cambiar la luz otra vez? (s/n): ")