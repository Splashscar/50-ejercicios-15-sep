class Candidato:
    def __init__(self, nombre, partido):
        self.nombre = nombre
        self.partido = partido
        self.votos = 0

    def agregar_voto(self):
        self.votos += 1


class Votante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ya_voto = False


class Eleccion:
    def __init__(self):
        self.candidatos = []
        self.votantes = []

    def agregar_candidato(self, candidato):
        self.candidatos.append(candidato)

    def agregar_votante(self, votante):
        self.votantes.append(votante)

    def votar(self, votante, candidato):
        if votante.ya_voto:
            print(f"{votante.nombre} ya votó, no puede votar de nuevo.")
        elif candidato not in self.candidatos:
            print("Ese candidato no está registrado.")
        else:
            candidato.agregar_voto()
            votante.ya_voto = True
            print(f"{votante.nombre} votó por {candidato.nombre}.")

    def mostrar_resultados(self):
        print("📊 Resultados de la elección:")
        for c in self.candidatos:
            print(f"{c.nombre} ({c.partido}): {c.votos} votos")
        ganador = max(self.candidatos, key=lambda x: x.votos)
        print(f"🏆 Ganador: {ganador.nombre} ({ganador.partido})")




eleccion = Eleccion()


c1 = Candidato("Ana", "Partido Azul")
c2 = Candidato("Luis", "Partido Verde")


eleccion.agregar_candidato(c1)
eleccion.agregar_candidato(c2)

v1 = Votante("Carlos")
v2 = Votante("María")
v3 = Votante("Pedro")

eleccion.agregar_votante(v1)
eleccion.agregar_votante(v2)
eleccion.agregar_votante(v3)

eleccion.votar(v1, c1)
eleccion.votar(v2, c2)
eleccion.votar(v3, c1)


eleccion.votar(v1, c2)


eleccion.mostrar_resultados()
