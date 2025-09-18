class estudiante:
    def __new__(self,nombre,edad,carrera):
        self.nombre = nombre
        self.edads =edad
        self.carrera =carrera

est1 = estudiante ("ana","20","ingeneria")
print(est1.nombre,est1.edad,est1.carrera)