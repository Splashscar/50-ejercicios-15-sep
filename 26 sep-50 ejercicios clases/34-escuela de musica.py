class Estudiante:
    def __init__(self, nombre, instrumento):
        self.nombre = nombre
        self.instrumento = instrumento
        self.progreso = 0  # porcentaje

    def practicar(self, horas):
        self.progreso += horas * 5  # cada hora suma 5%
        if self.progreso > 100:
            self.progreso = 100
        print(f"{self.nombre} practicó {horas}h. Progreso: {self.progreso}%")

    def mostrar_progreso(self):
        print(f"Estudiante: {self.nombre}, Instrumento: {self.instrumento}, Progreso: {self.progreso}%")


class Profesor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def enseñar(self, estudiante, tema):
        print(f"El profesor {self.nombre} enseñó {tema} a {estudiante.nombre}.")


class Clase:
    def __init__(self, materia, profesor, horario):
        self.materia = materia
        self.profesor = profesor
        self.horario = horario
        self.estudiantes = []

    def inscribir(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"{estudiante.nombre} se inscribió en {self.materia} con {self.profesor.nombre}.")

    def mostrar_clase(self):
        print(f"Clase: {self.materia} - Profesor: {self.profesor.nombre} ({self.profesor.especialidad})")
        print(f"Horario: {self.horario}")
        print("Estudiantes inscritos:")
        for e in self.estudiantes:
            print("-", e.nombre, f"({e.instrumento})")


prof = Profesor("Camilo", "Guitarra")


est1 = Estudiante("Laura", "Piano")
est2 = Estudiante("Mateo", "Guitarra")

clase1 = Clase("Música Avanzada", prof, "Lunes 4:00 PM")

clase1.inscribir(est1)
clase1.inscribir(est2)


clase1.mostrar_clase()


est1.practicar(3)
est2.practicar(5)


prof.enseñar(est1, "Armonía en piano")
prof.enseñar(est2, "Acordes de guitarra")


est1.mostrar_progreso()
est2.mostrar_progreso()
