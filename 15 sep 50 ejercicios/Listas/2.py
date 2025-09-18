class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

estudiantes = []

estudiantes.append(Estudiante("Ana", 20))
estudiantes.append(Estudiante("Luis", 22))
estudiantes.append(Estudiante("Sofía", 21))

for estudiante in estudiantes:
    estudiante.mostrar_info()