class Vehiculo:
    def __init__(self, modelo, año):
        self.info = (modelo, año)

    def mostrar(self):
        print(f"Modelo: {self.info[0]}, Año: {self.info[1]}")

v = Vehiculo("Toyota", 2022)
v.mostrar()
