class Vehiculo:
    def __init__(self, placa, capacidad):
        self.placa = placa
        self.capacidad = capacidad
        self.pasajeros = []

    def subir_pasajero(self, pasajero):
        if len(self.pasajeros) < self.capacidad:
            self.pasajeros.append(pasajero)
            print(f"{pasajero.nombre} subió al vehículo {self.placa}.")
        else:
            print("El vehículo está lleno.")

    def mostrar_pasajeros(self):
        print(f"Pasajeros en {self.placa}: {[p.nombre for p in self.pasajeros]}")


class Ruta:
    def __init__(self, nombre, horarios):
        self.nombre = nombre
        self.horarios = horarios  

    def mostrar_horarios(self):
        print(f"Ruta {self.nombre} tiene salidas en: {', '.join(self.horarios)}")


class Pasajero:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino



bus = Vehiculo("ABC-123", capacidad=2)
ruta1 = Ruta("Centro - Norte", ["8:00", "12:00", "18:00"])

p1 = Pasajero("Carlos", "Norte")
p2 = Pasajero("Ana", "Centro")
p3 = Pasajero("Luis", "Norte")


ruta1.mostrar_horarios()


bus.subir_pasajero(p1)
bus.subir_pasajero(p2)
bus.subir_pasajero(p3)  


bus.mostrar_pasajeros()
