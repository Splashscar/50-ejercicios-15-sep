class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

estudiantes = []

with open("estudiantes.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        if len(datos) == 2:
            nombre, edad = datos
            estudiantes.append(Estudiante(nombre, int(edad)))

for estudiante in estudiantes:
    estudiante.mostrar_info()