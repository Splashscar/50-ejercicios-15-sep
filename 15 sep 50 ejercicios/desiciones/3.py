class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def estado(self):
        if self.nota >= 3.0:
            return f"{self.nombre} aprobó con nota {self.nota}"
        else:
            return f"{self.nombre} reprobó con nota {self.nota}"


est = Estudiante("Maria", 2.8)
print(est.estado())
