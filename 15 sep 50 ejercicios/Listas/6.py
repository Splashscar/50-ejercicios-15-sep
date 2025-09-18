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

nombre_eliminar = "Luis"
estudiantes = [est for est in estudiantes if est.nombre != nombre_eliminar]

for estudiante in estudiantes:
    estudiante.mostrar_info()