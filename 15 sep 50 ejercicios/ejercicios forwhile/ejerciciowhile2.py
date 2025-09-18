class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, me llamo {self.nombre}!")

mi_persona = Persona("David")

continuar = "s"
while continuar.lower() == "s":
    mi_persona.saludar()
    continuar = input("¿Quieres saludar otra vez? (s/n): ")
