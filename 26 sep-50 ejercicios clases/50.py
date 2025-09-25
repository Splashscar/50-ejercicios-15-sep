import random

class Objeto:
    def __init__(self, nombre, peso, valor):
        self.nombre = nombre
        self.peso = peso
        self.valor = valor

    def __str__(self):
        return f"{self.nombre} (peso: {self.peso}, valor: {self.valor})"


class Avatar:
    def __init__(self, nombre, energia=100, monedas=50):
        self.nombre = nombre
        self.energia = energia
        self.monedas = monedas
        self.inventario = []

    def recoger(self, objeto):
        if self.energia >= objeto.peso:
            self.inventario.append(objeto)
            self.energia -= objeto.peso
            print(f"{self.nombre} recogió {objeto.nombre}. Energía restante: {self.energia}")
        else:
            print(f"{self.nombre} está demasiado cansado para recoger {objeto.nombre}.")

    def comprar(self, objeto):
        if self.monedas >= objeto.valor:
            self.monedas -= objeto.valor
            self.inventario.append(objeto)
            print(f"{self.nombre} compró {objeto.nombre}. Monedas restantes: {self.monedas}")
        else:
            print(f"{self.nombre} no tiene suficientes monedas para comprar {objeto.nombre}.")

    def vender(self, objeto):
        if objeto in self.inventario:
            self.inventario.remove(objeto)
            self.monedas += objeto.valor
            print(f"{self.nombre} vendió {objeto.nombre}. Monedas ahora: {self.monedas}")
        else:
            print(f"{objeto.nombre} no está en el inventario de {self.nombre}.")

    def __str__(self):
        return f"Avatar: {self.nombre}, Energía: {self.energia}, Monedas: {self.monedas}, Inventario: {[o.nombre for o in self.inventario]}"


class Mundo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.objetos_disponibles = []

    def generar_objetos(self):
        nombres = ["Espada", "Poción", "Escudo", "Manzana", "Mineral"]
        for _ in range(3):
            nombre = random.choice(nombres)
            peso = random.randint(1, 10)
            valor = random.randint(5, 20)
            self.objetos_disponibles.append(Objeto(nombre, peso, valor))

    def mostrar_objetos(self):
        print(f"Objetos en {self.nombre}:")
        for i, obj in enumerate(self.objetos_disponibles, 1):
            print(f"{i}. {obj}")


class Interaccion:
    @staticmethod
    def explorar(avatar, mundo):
        print(f"{avatar.nombre} explora el mundo {mundo.nombre}...")
        mundo.generar_objetos()
        mundo.mostrar_objetos()

    @staticmethod
    def recoger_objeto(avatar, mundo, indice):
        if 0 <= indice < len(mundo.objetos_disponibles):
            objeto = mundo.objetos_disponibles.pop(indice)
            avatar.recoger(objeto)
        else:
            print("Índice de objeto no válido.")



mundo = Mundo("Tierra Fantástica")
avatar = Avatar("Kai")

Interaccion.explorar(avatar, mundo)

Interaccion.recoger_objeto(avatar, mundo, 0)

espada = Objeto("Espada de Fuego", 5, 30)
avatar.comprar(espada)

avatar.vender(espada)

print(avatar)
