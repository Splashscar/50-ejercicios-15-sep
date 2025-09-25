class Habilidad:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

    def usar(self):
        return self.poder


class Item:
    def __init__(self, nombre, efecto):
        self.nombre = nombre
        self.efecto = efecto

    def aplicar(self, personaje):
        personaje.vida += self.efecto
        print(f"{personaje.nombre} usó {self.nombre} y recuperó {self.efecto} de vida.")


class Personaje:
    def __init__(self, nombre, vida=100, ataque=10):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.experiencia = 0

    def atacar(self, otro, habilidad=None):
        if habilidad:
            dano = self.ataque + habilidad.usar()
            print(f"{self.nombre} usa {habilidad.nombre}!")
        else:
            dano = self.ataque
        otro.vida -= dano
        print(f"{self.nombre} atacó a {otro.nombre} e hizo {dano} de daño.")

        self.ganar_experiencia(10)

    def ganar_experiencia(self, puntos):
        self.experiencia += puntos
        print(f"{self.nombre} ganó {puntos} puntos de experiencia. Total: {self.experiencia}")

    def mostrar_estado(self):
        print(f"{self.nombre} | Vida: {self.vida} | Ataque: {self.ataque} | Exp: {self.experiencia}")



espada = Item("Espada curativa", 20)
fuego = Habilidad("Bola de Fuego", 15)

p1 = Personaje("Guerrero")
p2 = Personaje("Orco", vida=80, ataque=8)

p1.mostrar_estado()
p2.mostrar_estado()

p1.atacar(p2, fuego)
p2.atacar(p1)

espada.aplicar(p1)

p1.mostrar_estado()
p2.mostrar_estado()
