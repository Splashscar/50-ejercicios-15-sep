class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __str__(self):
        return f"'{self.titulo}' de {self.autor}, publicado en {self.año}"

biblioteca = {}
biblioteca["001"] = Libro("Cien Años de Soledad", "García Márquez", 1967)
print(biblioteca["001"])
