class Planta:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia

    def __str__(self):
        return f"🌱 {self.nombre} (Energía: {self.energia})"


class Animal:
    def __init__(self, nombre, tipo, energia=100):
        self.nombre = nombre
        self.tipo = tipo  
        self.energia = energia

    def comer(self, alimento):
        if isinstance(alimento, Planta) and self.tipo in ["herbívoro", "omnívoro"]:
            self.energia += alimento.energia
            print(f"🐇 {self.nombre} comió {alimento.nombre} y ganó {alimento.energia} de energía.")
        elif isinstance(alimento, Animal) and self.tipo in ["carnívoro", "omnívoro"]:
            if alimento.energia > 0:  
                ganancia = alimento.energia // 2
                self.energia += ganancia
                alimento.energia = 0
                print(f"🦁 {self.nombre} cazó a {alimento.nombre} y ganó {ganancia} de energía.")
        else:
            print(f"⚠️ {self.nombre} no puede comer {alimento.nombre}.")

    def __str__(self):
        return f"🐾 {self.nombre} ({self.tipo}) - Energía: {self.energia}"


class Ambiente:
    def __init__(self, nombre, clima):
        self.nombre = nombre
        self.clima = clima
        self.animales = []
        self.plantas = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def agregar_planta(self, planta):
        self.plantas.append(planta)

    def estado(self):
        print(f"\n🌍 Ambiente: {self.nombre} ({self.clima})")
        print("Animales:")
        for a in self.animales:
            print(f"  - {a}")
        print("Plantas:")
        for p in self.plantas:
            print(f"  - {p}")


class CadenaAlimenticia:
    def __init__(self, ambiente):
        self.ambiente = ambiente

    def interactuar(self):
        """Simula interacciones de alimentación en el ambiente."""
        print("\n🔄 Simulación de interacciones en la cadena alimenticia...")
        for animal in self.ambiente.animales:
            if animal.tipo == "herbívoro" and self.ambiente.plantas:
                planta = self.ambiente.plantas.pop(0) 
                animal.comer(planta)

        for depredador in self.ambiente.animales:
            if depredador.tipo == "carnívoro":
                for presa in self.ambiente.animales:
                    if presa.tipo == "herbívoro" and presa.energia > 0:
                        depredador.comer(presa)
                        break 


selva = Ambiente("Selva Amazónica", "Húmedo Tropical")

pl1 = Planta("Arbusto", 20)
pl2 = Planta("Hierba", 10)

herb = Animal("Conejo", "herbívoro", energia=50)
carn = Animal("Lobo", "carnívoro", energia=80)
omn = Animal("Oso", "omnívoro", energia=70)

selva.agregar_planta(pl1)
selva.agregar_planta(pl2)
selva.agregar_animal(herb)
selva.agregar_animal(carn)
selva.agregar_animal(omn)

selva.estado()

cadena = CadenaAlimenticia(selva)
cadena.interactuar()

selva.estado()
