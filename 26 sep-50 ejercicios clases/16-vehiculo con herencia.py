class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def mostrar_info(self):
        print(f"Vehiculo: {self.marca} {self.modelo}")

class carro(vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Carro: {self.marca} {self.modelo},  Puertas: {self.puertas}")

class motocicleta(vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Motocicleta: {self.marca} {self.modelo}, cilindraje: {self.cilindraje}cc")

class bicicleta(vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Bicicleta: {self.marca} {self.modelo}, Tipo: {self.tipo}")

carro1 = carro("Toyota", "Corolla", 4)
moto = motocicleta("Yamaha", "YZF-R3", 321)
bici = bicicleta("Giant", "Escape 3", "Urbana")

carro1.mostrar_info()
moto.mostrar_info()
bici.mostrar_info()