class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

estudiantes = [
    Estudiante("Ana", 20),
    Estudiante("Luis", 22),
    Estudiante("Sofía", 21)
]

nombre_buscar = "Luis"
encontrado = False
for estudiante in estudiantes:
    if estudiante.nombre == nombre_buscar:
        estudiante.mostrar_info()
        encontrado = True

if not encontrado:
    print(f"Estudiante {nombre_buscar} no encontrado")