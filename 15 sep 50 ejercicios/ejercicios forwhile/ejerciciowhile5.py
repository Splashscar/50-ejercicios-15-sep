class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print(f"Hola, soy {self.nombre}")

personas = []

continuar = "s"
while continuar.lower() == "s":
    nombre = input("Ingresa un nombre: ")
    persona = Persona(nombre)
    personas.append(persona)
    continuar = input("¿Quieres agregar otra persona? (s/n): ")

print("\nPersonas registradas:")
for p in personas:
    p.presentarse()