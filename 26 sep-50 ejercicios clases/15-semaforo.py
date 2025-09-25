import time

class Semaforo:
    def __init__(self):
        self.estado = "rojo"   
        self.tiempos = {       
            "rojo": 5,
            "verde": 4,
            "amarillo": 2
        }

    def mostrar_estado(self):
        print(f"El semáforo está en {self.estado.upper()}")

    def cambiar_estado(self):
        if self.estado == "rojo":
            self.estado = "amarillo"
        elif self.estado == "amarillo":
            self.estado = "verde"
        elif self.estado == "verde":
            self.estado = "rojo"

    def iniciar(self, ciclos=3):
        """Ejecuta el semáforo por un número de ciclos"""
        for _ in range(ciclos):
            self.mostrar_estado()
            time.sleep(self.tiempos[self.estado])  
            self.cambiar_estado()

semaforo = Semaforo()
semaforo.iniciar()  

print("Simulación del semáforo finalizada.")