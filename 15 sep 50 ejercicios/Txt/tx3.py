class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def guardar_en_txt(self, nombre_archivo):
        with open(nombre_archivo, "a") as archivo:
            archivo.write(f"{self.nombre},{self.edad}\n")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))

nuevo_estudiante = Estudiante(nombre, edad)
nuevo_estudiante.guardar_en_txt("estudiantes.txt")
print("Estudiante agregado al archivo.")

with open("estudiantes.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        print(f"Nombre: {datos[0]}, Edad: {datos[1]}")