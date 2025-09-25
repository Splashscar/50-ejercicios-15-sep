class Materia:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

class Calificacion:
    def __init__(self, materia, nota):
        self.materia = materia
        self.nota = nota

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def agregar_calificacion(self, materia, nota):
        self.calificaciones.append(Calificacion(materia, nota))

    def promedio_ponderado(self):
        total_puntos = 0
        total_creditos = 0
        for c in self.calificaciones:
            total_puntos += c.nota * c.materia.creditos
            total_creditos += c.materia.creditos
        if total_creditos == 0:
            return 0
        return total_puntos / total_creditos

mate = Materia("Matemáticas", 4)
historia = Materia("Historia", 2)
programacion = Materia("Programación", 3)

e1 = Estudiante("Juan")


e1.agregar_calificacion(mate, 4.5)
e1.agregar_calificacion(historia, 3.0)
e1.agregar_calificacion(programacion, 5.0)

print("Promedio ponderado de", e1.nombre, ":", e1.promedio_ponderado())
