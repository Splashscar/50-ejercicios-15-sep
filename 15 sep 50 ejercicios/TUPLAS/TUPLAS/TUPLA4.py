class Libro:
    def __init__(self, titulo, autor):
        self.info = (titulo, autor)

    def mostrar(self):
        print(f"Título: {self.info[0]}, Autor: {self.info[1]}")

libro = Libro("Python Básico", "Juan Pérez")
libro.mostrar()
