class Pelicula:
    def __init__(self, titulo, director, año):
        self.titulo = titulo
        self.director = director
        self.año = año

    def __str__(self):
        return f"Pelicula: {self.titulo}, Director: {self.director}, Año: {self.año}"

peliculas = {}
peliculas["P001"] = Pelicula("Inception", "Christopher Nolan", 2010)
print(peliculas["P001"])
