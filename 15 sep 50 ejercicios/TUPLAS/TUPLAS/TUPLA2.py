class Persona:
    def __init__(self, nombre, edad):
        self.datos = (nombre, edad)

    def mostrar(self):
        print(f"Nombre: {self.datos[0]}, Edad: {self.datos[1]}")

p1 = Persona("Alexis", 20)
p1.mostrar()
