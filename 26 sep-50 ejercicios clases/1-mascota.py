class Mascota:
    def __init__ (self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    def presentarse(self):
        print (f"Hola, soy {self.nombre}, un {self.especie} de {self.edad} años.")

mascota1 = Mascota("Firulais", "Perro", 3)
mascota2 = Mascota("Michi", "Gato", 2)
mascota3 = Mascota("Nemo", "Pez", 1)

print(mascota1.presentarse())
print(mascota2.presentarse())
print(mascota3.presentarse())