class Huesped:
    def __init__(self, nombre):
        self.nombre = nombre


class Habitacion:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
        self.disponible = True

    def ocupar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True


class Reserva:
    def __init__(self, huesped, habitacion, noches):
        self.huesped = huesped
        self.habitacion = habitacion
        self.noches = noches
        self.total = habitacion.precio * noches

    def mostrar_reserva(self):
        print(f"Reserva de {self.huesped.nombre}: Habitación {self.habitacion.numero}, "
              f"{self.noches} noches - Total: ${self.total}")


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_disponibles(self):
        print(f"🏨 Habitaciones disponibles en {self.nombre}:")
        for h in self.habitaciones:
            if h.disponible:
                print(f"Habitación {h.numero} - Precio: ${h.precio}")

    def reservar(self, huesped, numero_habitacion, noches):
        for h in self.habitaciones:
            if h.numero == numero_habitacion and h.disponible:
                h.ocupar()
                reserva = Reserva(huesped, h, noches)
                print(f"✅ Reserva confirmada para {huesped.nombre} en habitación {h.numero}")
                return reserva
        print("❌ La habitación no está disponible.")
        return None



hotel = Hotel("Hotel Paraíso")


hotel.agregar_habitacion(Habitacion(101, 200))
hotel.agregar_habitacion(Habitacion(102, 250))
hotel.agregar_habitacion(Habitacion(103, 300))

huesped1 = Huesped("María")

hotel.mostrar_disponibles()


reserva1 = hotel.reservar(huesped1, 102, 3)


if reserva1:
    reserva1.mostrar_reserva()


huesped2 = Huesped("Pedro")
hotel.reservar(huesped2, 102, 2)


hotel.mostrar_disponibles()
