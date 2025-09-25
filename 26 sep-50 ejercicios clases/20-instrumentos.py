class instrumento:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
class guitarra(instrumento):
    def __init__(self, nombre, tipo, cuerdas):
        super().__init__(nombre, tipo)
        self.cuerdas = cuerdas

    def tocar(self):
        print(f"Tocando la {self.nombre}, que es un instrumento de tipo {self.tipo}.")
        return f"Tiene {self.cuerdas} cuerdas."
    
class piano(instrumento):
    def __init__(self, nombre, tipo, teclas):
        super().__init__(nombre, tipo)
        self.teclas = teclas

    def tocar(self):
        print(f"Tocando el {self.nombre}, que es un instrumento de tipo {self.tipo}.")
        return f" Tiene {self.teclas} teclas."
    
class bateria(instrumento):
    def __init__(self, nombre, tipo, tamano):
        super().__init__(nombre, tipo)
        self.tamano = tamano

    def tocar(self):
        print(f"Tocando la {self.nombre}, que es un instrumento de tipo {self.tipo}.")
        return f" Es de tamaño {self.tamano}."
    
guitarra1 = guitarra("Guitarra Eléctrica", "Cuerda", 6)
piano1 = piano("Piano de Cola", "Teclado", 88)
bateria1 = bateria("Batería Acústica", "Percusión", "Grande")
print(guitarra1.tocar())
print(piano1.tocar())
print(bateria1.tocar())
