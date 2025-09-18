class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def guardar_en_txt(self, nombre_archivo):
        with open(nombre_archivo, "a") as archivo:
            archivo.write(f"{self.nombre},{self.edad}\n")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

estudiantes = [
    Estudiante("Ana", 20),
    Estudiante("Luis", 22),
    Estudiante("Sofía", 21)
]

for estudiante in estudiantes:
    estudiante.guardar_en_txt("estudiantes.txt")

print("Estudiantes guardados en estudiantes.txt")