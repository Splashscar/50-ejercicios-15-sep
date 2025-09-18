class Estudiante:
    def __init__(self, nombre, notas):
        self.info = (nombre, tuple(notas))

    def mostrar(self):
        print(f"Estudiante: {self.info[0]}, Notas: {self.info[1]}")

est = Estudiante("Ana", [5, 4, 3])
est.mostrar()
