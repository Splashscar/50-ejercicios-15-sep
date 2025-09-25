from datetime import datetime


class Tratamiento:
    def __init__(self, descripcion, medicamento, duracion_dias):
        self.descripcion = descripcion
        self.medicamento = medicamento
        self.duracion_dias = duracion_dias
        self.fecha_inicio = datetime.now()

    def __str__(self):
        return (f"Tratamiento: {self.descripcion}, "
                f"Medicamento: {self.medicamento}, "
                f"Duración: {self.duracion_dias} días, "
                f"Inicio: {self.fecha_inicio.strftime('%Y-%m-%d')}")


class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def __str__(self):
        return f"Departamento: {self.nombre}, Doctores: {[d.nombre for d in self.doctores]}"


class Doctor:
    def __init__(self, nombre, especialidad, departamento=None):
        self.nombre = nombre
        self.especialidad = especialidad
        self.departamento = departamento
        if departamento:
            departamento.agregar_doctor(self)

    def atender_paciente(self, paciente, diagnostico, tratamiento):
        registro = {
            "fecha": datetime.now(),
            "doctor": self.nombre,
            "especialidad": self.especialidad,
            "diagnostico": diagnostico,
            "tratamiento": tratamiento
        }
        paciente.historial.append(registro)
        print(f"✔️ El Dr. {self.nombre} atendió a {paciente.nombre}: {diagnostico}")

    def __str__(self):
        return f"Dr. {self.nombre} ({self.especialidad})"


class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.historial = []

    def mostrar_historial(self):
        print(f"\n📋 Historial Médico de {self.nombre}:")
        if not self.historial:
            print("No hay registros médicos.")
        for registro in self.historial:
            print(f"- Fecha: {registro['fecha'].strftime('%Y-%m-%d %H:%M')}")
            print(f"  Doctor: {registro['doctor']} ({registro['especialidad']})")
            print(f"  Diagnóstico: {registro['diagnostico']}")
            print(f"  {registro['tratamiento']}")
            print("----------------------------------")

    def __str__(self):
        return f"Paciente: {self.nombre}, Edad: {self.edad}"
    


cardiologia = Departamento("Cardiología")
neurologia = Departamento("Neurología")

dr_gomez = Doctor("Gómez", "Cardiólogo", cardiologia)
dr_ruiz = Doctor("Ruiz", "Neurólogo", neurologia)

paciente1 = Paciente("Laura Martínez", 45)

trat1 = Tratamiento("Arritmia", "Amiodarona", 30)
dr_gomez.atender_paciente(paciente1, "Arritmia detectada", trat1)

trat2 = Tratamiento("Migraña crónica", "Sumatriptán", 15)
dr_ruiz.atender_paciente(paciente1, "Dolores de cabeza frecuentes", trat2)

paciente1.mostrar_historial()
