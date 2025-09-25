class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.historial = []  

    def agregar_historial(self, nota):
        self.historial.append(nota)

    def mostrar_historial(self):
        print(f"Historial de {self.nombre}:")
        for h in self.historial:
            print("-", h)


class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def atender(self, paciente, nota):
        paciente.agregar_historial(f"Dr. {self.nombre}: {nota}")
        print(f"El doctor {self.nombre} atendió a {paciente.nombre}.")


class Cita:
    def __init__(self, paciente, doctor, fecha, hora):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora

    def mostrar_cita(self):
        print(f"Cita: {self.fecha} {self.hora} - {self.paciente.nombre} con Dr. {self.doctor.nombre}")



pac1 = Paciente("Laura", 30)
doc1 = Doctor("Ramírez", "Cardiología")

cita1 = Cita(pac1, doc1, "2025-09-25", "10:00 AM")
cita1.mostrar_cita()


doc1.atender(pac1, "Chequeo de presión arterial. Todo normal.")

pac1.mostrar_historial()
