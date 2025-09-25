class carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor} de {self.palo}"

class baraja:
    def __init__(self):
        self.cartas = []
        palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for palo in palos:
            for valor in valores:
                self.cartas.append(carta(valor, palo))

    def barajar(self):
        import random
        random.shuffle(self.cartas)
    def repartir_carta(self):
        return self.cartas.pop() if self.cartas else None

class mano:
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def mostrar_mano(self):
        return ', '.join(str(carta) for carta in self.cartas)
    
baraja1 = baraja()
baraja1.barajar()
mano1 = mano()
for _ in range(5):
    carta_repartida = baraja1.repartir_carta()
    if carta_repartida:
        mano1.agregar_carta(carta_repartida)
print("Cartas en la mano:", mano1.mostrar_mano())
mano2 = mano()
for _ in range(5):
    carta_repartida = baraja1.repartir_carta()
    if carta_repartida:
        mano2.agregar_carta(carta_repartida)
print("Cartas en la mano:", mano2.mostrar_mano())
mano3 = mano()
for _ in range(5):
    carta_repartida = baraja1.repartir_carta()
    if carta_repartida:
        mano3.agregar_carta(carta_repartida)
print("Cartas en la mano:", mano3.mostrar_mano())