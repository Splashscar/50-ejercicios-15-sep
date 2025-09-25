class estudiante:
    def __init__(self, nombre, edad,notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas
    def promedio(self, notas):
        promedio = sum(notas) / len(notas)
        print(f"El promedio de {self.nombre} es: {promedio}")

estudiante1 = estudiante("Ana", 20, [85, 90, 78])
estudiante2 = estudiante("Luis", 22, [88, 76, 92])
estudiante3 = estudiante("Maria", 19, [90, 91, 89])

estudiante1.promedio(estudiante1.notas)
estudiante2.promedio(estudiante2.notas)
estudiante3.promedio(estudiante3.notas)
