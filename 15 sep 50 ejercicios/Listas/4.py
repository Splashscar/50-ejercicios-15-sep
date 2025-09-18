class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Nota: {self.nota}")

class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        print(f"Estudiantes del curso {self.nombre_curso}:")
        for est in self.estudiantes:
            est.mostrar_info()

    def buscar_estudiante(self, nombre):
        for est in self.estudiantes:
            if est.nombre == nombre:
                return est
        return None

curso_python = Curso("Python Básico")
curso_python.agregar_estudiante(Estudiante("Ana", 20, 9.5))
curso_python.agregar_estudiante(Estudiante("Luis", 22, 8.7))
curso_python.agregar_estudiante(Estudiante("Sofía", 21, 10))

curso_python.mostrar_estudiantes()

resultado = curso_python.buscar_estudiante("Luis")
if resultado:
    print("Estudiante encontrado:")
    resultado.mostrar_info()
else:
    print("Estudiante no encontrado")