class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_aumento(self):
        if self.salario < 2000:
            return f"{self.nombre} recibe aumento del 20%. Nuevo salario: {self.salario * 1.2}"
        elif self.salario <= 5000:
            return f"{self.nombre} recibe aumento del 10%. Nuevo salario: {self.salario * 1.1}"
        else:
            return f"{self.nombre} no recibe aumento. Salario actual: {self.salario}"


empleado = Empleado("Carlos", 1800)
print(empleado.calcular_aumento())
