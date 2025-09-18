class jugadores:
    def __init__(self, balon, equipo, uniformes):
                 self.balon = balon
                 self.equipo = equipo
                 self.uniformes = uniformes
estadio = jugadores("guayos", "nacional", "atanasio" )
print(estadio.balon, estadio.equipo, estadio.uniformes)
jugadores = ["messi","cristiano","neymar","mbappe"]
print("lista de jugadores en el equipo")
for estadios in jugadores:
      print("entrenador",estadio)