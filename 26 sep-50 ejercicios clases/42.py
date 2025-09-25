from datetime import datetime
import random

class Contenido:
    def __init__(self, titulo, genero, duracion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion  # minutos
        self.reproducciones = 0
    
    def reproducir(self):
        self.reproducciones += 1
        return f"▶️ Reproduciendo {self.titulo} ({self.duracion} min)"
    
    def __str__(self):
        return f"{self.titulo} - {self.genero} ({self.duracion} min, {self.reproducciones} rep.)"


class Playlist:
    def __init__(self, nombre, creador):
        self.nombre = nombre
        self.creador = creador
        self.contenidos = []
    
    def agregar_contenido(self, contenido):
        self.contenidos.append(contenido)
    
    def mostrar(self):
        print(f"🎵 Playlist: {self.nombre} (creada por {self.creador.nombre})")
        for c in self.contenidos:
            print(" -", c)


class Suscripcion:
    def __init__(self, tipo="gratis"):
        self.tipo = tipo  # gratis, premium, familiar
        self.fecha_inicio = datetime.now()
    
    def __str__(self):
        return f"Suscripción {self.tipo.capitalize()} desde {self.fecha_inicio.strftime('%Y-%m-%d')}"


class Usuario:
    def __init__(self, nombre, suscripcion=None):
        self.nombre = nombre
        self.suscripcion = suscripcion if suscripcion else Suscripcion("gratis")
        self.historial = []  # contenidos escuchados
        self.estadisticas = {}  # genero: tiempo total
    
    def escuchar(self, contenido):
        print(contenido.reproducir())
        self.historial.append(contenido)
        self.estadisticas[contenido.genero] = self.estadisticas.get(contenido.genero, 0) + contenido.duracion
    
    def recomendar(self, catalogo):
        if not self.estadisticas:
            return random.choice(catalogo)
        genero_fav = max(self.estadisticas, key=self.estadisticas.get)
        candidatos = [c for c in catalogo if c.genero == genero_fav]
        return random.choice(candidatos) if candidatos else random.choice(catalogo)
    
    def mostrar_estadisticas(self):
        print(f"📊 Estadísticas de {self.nombre}:")
        for genero, tiempo in self.estadisticas.items():
            print(f" - {genero}: {tiempo} min escuchados")
    
    def __str__(self):
        return f"{self.nombre} | {self.suscripcion}"



c1 = Contenido("Canción A", "Pop", 3)
c2 = Contenido("Canción B", "Rock", 4)
c3 = Contenido("Podcast X", "Educativo", 30)
c4 = Contenido("Canción C", "Pop", 5)

catalogo = [c1, c2, c3, c4]

u1 = Usuario("María", Suscripcion("premium"))
u2 = Usuario("Pedro") 

p1 = Playlist("Favoritos Pop", u1)
p1.agregar_contenido(c1)
p1.agregar_contenido(c4)

p1.mostrar()

u1.escuchar(c1)
u1.escuchar(c4)
u1.escuchar(c3)

u2.escuchar(c2)
u2.escuchar(c2)

print("\n✨ Recomendación para María:", u1.recomendar(catalogo))
print("✨ Recomendación para Pedro:", u2.recomendar(catalogo))

print("\n")
u1.mostrar_estadisticas()
u2.mostrar_estadisticas()
