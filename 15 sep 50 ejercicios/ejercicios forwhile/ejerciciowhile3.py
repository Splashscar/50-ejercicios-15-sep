class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def jugar(self):
        print(f"{self.nombre} está jugando!")

nombre_mascota = input("Ingresa el nombre de tu mascota: ")
mascota = Mascota(nombre_mascota)

continuar = "s"
while continuar.lower() == "s":
    mascota.jugar()
    continuar = input("¿Quieres que juegue otra vez? (s/n): ")