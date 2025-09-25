import datetime

class Recurso:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  # Ej: "Sala", "Equipo", "Servicio"
        self.disponible = True

    def __str__(self):
        return f"{self.tipo}: {self.nombre} ({'Disponible' if self.disponible else 'Reservado'})"


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = []

    def reservar(self, recurso, fecha, hora):
        if recurso.disponible:
            reserva = Reserva(self, recurso, fecha, hora)
            self.reservas.append(reserva)
            recurso.disponible = False
            return reserva
        else:
            print("❌ El recurso no está disponible.")

    def mostrar_reservas(self):
        for r in self.reservas:
            print(r)


class Reserva:
    def __init__(self, usuario, recurso, fecha, hora):
        self.usuario = usuario
        self.recurso = recurso
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return (f"{self.usuario.nombre} reservó {self.recurso.nombre} "
                f"({self.recurso.tipo}) para el {self.fecha} a las {self.hora}")
    

sala1 = Recurso("Sala de reuniones A", "Sala")
equipo1 = Recurso("Proyector HD", "Equipo")

u1 = Usuario("Laura")


res1 = u1.reservar(sala1, "2025-09-25", "10:00 AM")
res2 = u1.reservar(equipo1, "2025-09-25", "10:00 AM")


u1.mostrar_reservas()


u1.reservar(sala1, "2025-09-26", "3:00 PM")

