class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
encontrado = False

with open("estudiantes.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        if datos[0].lower() == nombre_buscar.lower():
            estudiante = Estudiante(datos[0], int(datos[1]))
            estudiante.mostrar_info()
            encontrado = True

if not encontrado:
    print(f"Estudiante {nombre_buscar} no encontrado")