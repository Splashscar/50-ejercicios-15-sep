class empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_detalles(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}"
    
class empleado_tiempo_completo(empleado):
    def __init__(self, nombre, salario, beneficios):
        super().__init__(nombre, salario)
        self.beneficios = beneficios

    def mostrar_detalles(self):
        detalles_base = super().mostrar_detalles()
        return f"{detalles_base}, Beneficios: {self.beneficios}"
    
class empleado_medio_tiempo(empleado):
    def __init__(self, nombre, salario, horas_trabajadas):
        super().__init__(nombre, salario)
        self.horas_trabajadas = horas_trabajadas

    def mostrar_detalles(self):
        detalles_base = super().mostrar_detalles()
        return f"{detalles_base}, Horas Trabajadas: {self.horas_trabajadas}"
    
Valor_hora = 6471
print("Que tipo de empleado eres?: ")
print("1. Empleado a tiempo completo")
print("2. Empleado a medio tiempo")
opcion = input("Ingrese la opcion (1/2): ")
if opcion == '1':
    nombre = input("Ingrese su nombre: ")
    horas = int(input("Ingrese las horas trabajadas al mes: "))
    salario = Valor_hora * horas
    beneficios = input("Ingrese los beneficios adicionales (por ejemplo: Seguro de salud, vacaciones etc): ")
    empleado1 = empleado_tiempo_completo(nombre, salario, beneficios)
    print(empleado1.mostrar_detalles())
elif opcion == '2':
    nombre = input("Ingrese su nombre: ")
    horas = int(input("Ingrese las horas trabajadas al mes: "))
    salario = Valor_hora * horas
    empleado2 = empleado_medio_tiempo(nombre, salario, horas)
    print(empleado2.mostrar_detalles())