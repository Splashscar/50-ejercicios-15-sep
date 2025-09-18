class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} es un {self.especie} de {self.edad} años"

mascotas = {}
mascotas["001"] = Mascota("Firulais", "Perro", 5)
print(mascotas["001"])
