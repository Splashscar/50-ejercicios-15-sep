class Vehiculo:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad

    def tipo(self):
        if self.velocidad <= 40:
            return f"{self.marca} es un vehículo lento."
        elif self.velocidad <= 100:
            return f"{self.marca} es un vehículo normal."
        else:
            return f"{self.marca} es un vehículo rápido."


carro = Vehiculo("Toyota", 120)
print(carro.tipo())
