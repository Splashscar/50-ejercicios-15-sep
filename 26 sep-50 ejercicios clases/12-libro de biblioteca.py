class libro:
    def __init__ (self, titulo, autor, ISBN, estado):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.estado = estado

    def prestar(self):
        if self.estado == "disponible":
            self.estado = "prestado"
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible para prestar.")
    def devolver(self):
        if self.estado == "prestado":
            self.estado = "disponible"
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

    def mostrar_libros(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.ISBN}, Estado: {self.estado}")

libro1 = libro("Cien Años de Soledad", "Gabriel García Márquez", "978-3-16-148410-0", "disponible")
libro2 = libro("1984", "George Orwell", "978-0-452-28423-4", "prestado")
libro3 = libro("El Principito", "Antoine de Saint-Exupéry", "978-0-15-601219-5", "disponible")

print(libro1.mostrar_libros())
print(libro2.mostrar_libros())
print(libro3.mostrar_libros())

accion = print("Que te gustaria hacer?: ")
print("1. Prestar libro")
print("2. Devolver libro")
opcion = input("Ingrese la opcion (1/2): ")
if opcion == '1':
    libro1.prestar()
elif opcion == '2':
    libro2.devolver()
    

