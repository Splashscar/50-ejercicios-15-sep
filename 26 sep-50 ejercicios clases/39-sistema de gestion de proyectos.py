from datetime import datetime, timedelta

class Empleado:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
    
    def __str__(self):
        return f"{self.nombre} ({self.rol})"

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
    
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    
    def mostrar_empleados(self):
        return [str(e) for e in self.empleados]

class Tarea:
    def __init__(self, titulo, duracion_dias):
        self.titulo = titulo
        self.duracion = timedelta(days=duracion_dias)
        self.dependencias = []
        self.fecha_inicio = None
        self.fecha_fin = None
        self.asignado = None
    
    def agregar_dependencia(self, tarea):
        self.dependencias.append(tarea)
    
    def asignar_empleado(self, empleado):
        self.asignado = empleado
    
    def calcular_fechas(self, fecha_inicio_proyecto):
        if self.dependencias:
            ultima = max([t.fecha_fin for t in self.dependencias])
            self.fecha_inicio = ultima
        else:
            self.fecha_inicio = fecha_inicio_proyecto
        self.fecha_fin = self.fecha_inicio + self.duracion
    
    def __str__(self):
        asignado = self.asignado.nombre if self.asignado else "Sin asignar"
        return f"Tarea: {self.titulo} | Inicio: {self.fecha_inicio.date()} | Fin: {self.fecha_fin.date()} | Responsable: {asignado}"

class Proyecto:
    def __init__(self, nombre, fecha_inicio):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.tareas = []
        self.equipos = []
    
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
    
    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)
    
    def generar_cronograma(self):
        for tarea in self.tareas:
            tarea.calcular_fechas(self.fecha_inicio)
    
    def mostrar_cronograma(self):
        print(f"\n📅 Cronograma del proyecto '{self.nombre}':")
        for tarea in sorted(self.tareas, key=lambda t: t.fecha_inicio):
            print(tarea)



juan = Empleado("Juan", "Desarrollador")
maria = Empleado("María", "Diseñadora")
pedro = Empleado("Pedro", "Tester")


equipo_dev = Equipo("Equipo Dev")
equipo_dev.agregar_empleado(juan)
equipo_dev.agregar_empleado(maria)
equipo_dev.agregar_empleado(pedro)

t1 = Tarea("Diseño UI", 5)
t2 = Tarea("Backend API", 7)
t3 = Tarea("Frontend", 6)
t4 = Tarea("Pruebas", 4)


t2.agregar_dependencia(t1)  # Backend depende del diseño
t3.agregar_dependencia(t1)  # Frontend depende del diseño
t4.agregar_dependencia(t2)  # Pruebas dependen del backend
t4.agregar_dependencia(t3)  # y del frontend

t1.asignar_empleado(maria)
t2.asignar_empleado(juan)
t3.asignar_empleado(juan)
t4.asignar_empleado(pedro)

proyecto = Proyecto("Sistema de Gestión", datetime(2025, 10, 1))
proyecto.agregar_equipo(equipo_dev)
proyecto.agregar_tarea(t1)
proyecto.agregar_tarea(t2)
proyecto.agregar_tarea(t3)
proyecto.agregar_tarea(t4)

proyecto.generar_cronograma()
proyecto.mostrar_cronograma()
