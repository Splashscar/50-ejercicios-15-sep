class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

nombre_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")

lineas_actualizadas = []
encontrado = False

with open("estudiantes.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        if datos[0].lower() != nombre_eliminar.lower():
            lineas_actualizadas.append(linea)
        else:
            encontrado = True

with open("estudiantes.txt", "w") as archivo:
    archivo.writelines(lineas_actualizadas)

if encontrado:
    print(f"Estudiante {nombre_eliminar} eliminado.")
else:
    print(f"Estudiante {nombre_eliminar} no encontrado.")

with open("estudiantes.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        estudiante = Estudiante(datos[0], int(datos[1]))
        estudiante.mostrar_info()