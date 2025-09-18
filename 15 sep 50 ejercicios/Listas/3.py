class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Nota: {self.nota}")

estudiantes = [
    Estudiante("Ana", 20, 9.5),
    Estudiante("Luis", 22, 8.7),
    Estudiante("Sofía", 21, 10)
]

total_notas = 0
for estudiante in estudiantes:
    estudiante.mostrar_info()
    total_notas += estudiante.nota

promedio = total_notas / len(estudiantes)
print(f"Promedio de notas: {promedio}")