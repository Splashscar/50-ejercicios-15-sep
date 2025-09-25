from abc import ABC, abstractmethod
import math

class Forma(ABC):
    """Clase base abstracta para cualquier forma geométrica."""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Poligono(Forma):
    """Clase base para polígonos. No implementa area/perimetro por sí misma."""
    def __init__(self, lados):
        """
        lados: lista o tupla con longitudes de los lados (en orden cualquiera).
        Para polígonos regulares, todos los valores pueden ser iguales.
        """
        if not lados or any(l <= 0 for l in lados):
            raise ValueError("La lista de lados debe contener valores positivos.")
        self.lados = list(lados)

    def perimetro(self):
        return sum(self.lados)


class Triangulo(Poligono):
    """
    Triángulo definido por sus 3 lados (a, b, c).
    Area por la fórmula de Herón.
    """
    def __init__(self, a, b, c):
        lados = (a, b, c)
        super().__init__(lados)
        a, b, c = self.lados
        # Validación desigualdad triangular
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Las longitudes no cumplen la desigualdad triangular.")

    def area(self):
        a, b, c = self.lados
        s = (a + b + c) / 2.0  # semiperímetro
        # Herón: área = sqrt(s*(s-a)*(s-b)*(s-c))
        area_val = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area_val

    # perimetro() viene de Poligono (suma de lados)


class Cuadrado(Poligono):
    """
    Cuadrado regular: se le da la longitud del lado.
    """
    def __init__(self, lado):
        super().__init__([lado, lado, lado, lado])
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    # perimetro() viene de Poligono (5) -> aquí suma de 4 lados


class Pentagono(Poligono):
    """
    Pentágono regular (todos los lados iguales).
    Parámetro: lado (a).
    Fórmula del área para pentágono regular:
      area = (1/4) * sqrt(5 * (5 + 2*sqrt(5))) * a^2
    Perímetro = 5 * a
    """
    def __init__(self, lado):
        super().__init__([lado] * 5)
        self.lado = lado

    def area(self):
        a = self.lado
        factor = math.sqrt(5 * (5 + 2 * math.sqrt(5)))
        area_val = 0.25 * factor * a * a
        return area_val

    # perimetro() viene de Poligono

t = Triangulo(3, 4, 5)
print("Triángulo - perímetro:", t.perimetro(), "área:", t.area())

c = Cuadrado(4)
print("Cuadrado - perímetro:", c.perimetro(), "área:", c.area())

p = Pentagono(2)
print("Pentágono regular - perímetro:", p.perimetro(), "área:", p.area())
 