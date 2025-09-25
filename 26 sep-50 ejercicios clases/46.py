class Propuesta:
    def __init__(self, freelancer, monto, descripcion):
        self.freelancer = freelancer
        self.monto = monto
        self.descripcion = descripcion
        self.estado = "Pendiente"  # Pendiente, Aceptada, Rechazada

    def __str__(self):
        return f"💼 Propuesta de {self.freelancer.nombre} por ${self.monto} - {self.estado}"


class Proyecto:
    def __init__(self, titulo, descripcion, cliente):
        self.titulo = titulo
        self.descripcion = descripcion
        self.cliente = cliente
        self.propuestas = []
        self.freelancer_asignado = None
        self.completado = False

    def recibir_propuesta(self, propuesta):
        self.propuestas.append(propuesta)
        print(f"📩 Proyecto '{self.titulo}' recibió una propuesta de {propuesta.freelancer.nombre}.")

    def aceptar_propuesta(self, propuesta):
        if propuesta in self.propuestas:
            propuesta.estado = "Aceptada"
            self.freelancer_asignado = propuesta.freelancer
            print(f"✅ Propuesta aceptada: {propuesta.freelancer.nombre} trabajará en '{self.titulo}'.")

    def completar(self):
        if self.freelancer_asignado:
            self.completado = True
            print(f"🏁 Proyecto '{self.titulo}' completado por {self.freelancer_asignado.nombre}.")

    def __str__(self):
        return f"Proyecto: {self.titulo} - Cliente: {self.cliente.nombre}"


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.proyectos = []

    def publicar_proyecto(self, titulo, descripcion):
        proyecto = Proyecto(titulo, descripcion, self)
        self.proyectos.append(proyecto)
        print(f"📝 {self.nombre} publicó el proyecto '{titulo}'.")
        return proyecto

    def calificar_freelancer(self, freelancer, puntuacion):
        if 1 <= puntuacion <= 5:
            freelancer.recibir_calificacion(puntuacion)
            print(f"⭐ {self.nombre} calificó a {freelancer.nombre} con {puntuacion} estrellas.")


class Freelancer:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def enviar_propuesta(self, proyecto, monto, descripcion):
        propuesta = Propuesta(self, monto, descripcion)
        proyecto.recibir_propuesta(propuesta)
        return propuesta

    def recibir_calificacion(self, puntuacion):
        self.calificaciones.append(puntuacion)

    def promedio_calificaciones(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def __str__(self):
        return f"Freelancer: {self.nombre} - Calificación promedio: {self.promedio_calificaciones():.2f}"


cliente1 = Cliente("Ana")
freelancer1 = Freelancer("Carlos")
freelancer2 = Freelancer("Lucía")

proyecto1 = cliente1.publicar_proyecto("Página Web", "Crear una web para e-commerce.")

prop1 = freelancer1.enviar_propuesta(proyecto1, 500, "Tengo experiencia en tiendas online.")
prop2 = freelancer2.enviar_propuesta(proyecto1, 450, "Puedo hacerlo rápido y con buena calidad.")

proyecto1.aceptar_propuesta(prop2)

proyecto1.completar()

cliente1.calificar_freelancer(freelancer2, 5)

print(freelancer2)
