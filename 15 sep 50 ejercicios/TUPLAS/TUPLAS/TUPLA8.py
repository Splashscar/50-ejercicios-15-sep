class Cancion:
    def __init__(self, titulo, duracion):
        self.info = (titulo, duracion)

    def mostrar(self):
        print(f"Canción: {self.info[0]}, Duración: {self.info[1]} min")

c = Cancion("Mi canción", 4)
c.mostrar()
