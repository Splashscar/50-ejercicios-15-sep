class reloj:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def ajustar(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def avanzar(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
            if self.minutos >= 60:
                self.minutos = 0
                self.horas += 1
                if self.horas >= 24:
                    self.horas = 0

    def mostrar(self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
    
mi_reloj = reloj()
mi_reloj.ajustar(23, 59, 58)

print("Reloj digital:")
print(mi_reloj.mostrar())

print("Que quiere hacer?: ")
print("1. Ajustar hora")
print("2. Ver formato 24 horas")
opcion = input("Ingrese la opcion (1/2): ")
if opcion == '1':
    horas = int(input("Ingrese las horas (0-23): "))
    minutos = int(input("Ingrese los minutos (0-59): "))
    segundos = int(input("Ingrese los segundos (0-59): "))
    mi_reloj.ajustar(horas, minutos, segundos)
    print("Hora ajustada:", mi_reloj.mostrar())
elif opcion == '2':
    print("Hora en formato 24 horas:", mi_reloj.mostrar())


