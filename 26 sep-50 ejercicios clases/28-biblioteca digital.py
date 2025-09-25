import datetime

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({'Disponible' if self.disponible else 'Prestado'})"


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prestamos = []

    def pedir_libro(self, libro, dias=7):
        if libro.disponible:
            prestamo = Prestamo(self, libro, dias)
            self.prestamos.append(prestamo)
            libro.disponible = False
            return prestamo
        else:
            print("El libro no está disponible.")

    def mostrar_prestamos(self):
        for p in self.prestamos:
            print(p)


class Prestamo:
    def __init__(self, usuario, libro, dias):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = datetime.date.today()
        self.fecha_vencimiento = self.fecha_prestamo + datetime.timedelta(days=dias)

    def calcular_multa(self):
        hoy = datetime.date.today()
        if hoy > self.fecha_vencimiento:
            dias_retraso = (hoy - self.fecha_vencimiento).days
            return dias_retraso * 1000 
        return 0

    def __str__(self):
        return (f"{self.libro.titulo} prestado a {self.usuario.nombre} | "
                f"Vence: {self.fecha_vencimiento} | Multa: {self.calcular_multa()}")



lib1 = Libro("Cien Años de Soledad", "Gabriel García Márquez")
lib2 = Libro("El Quijote", "Miguel de Cervantes")


u1 = Usuario("Juan")


prestamo1 = u1.pedir_libro(lib1, dias=5)


u1.mostrar_prestamos()
