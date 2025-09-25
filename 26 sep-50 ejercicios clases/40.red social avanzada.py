from datetime import datetime

# ------------------ CLASES BASE ------------------

class Usuario:
    def __init__(self, nombre, privacidad="publico"):
        self.nombre = nombre
        self.amigos = []
        self.mensajes = []
        self.notificaciones = []
        self.privacidad = privacidad  # "publico", "amigos", "privado"
    
    def agregar_amigo(self, usuario):
        if usuario not in self.amigos:
            self.amigos.append(usuario)
            usuario.amigos.append(self)
            self.recibir_notificacion(f"{usuario.nombre} ahora es tu amigo 🤝")
    
    def enviar_mensaje(self, destinatario, contenido):
        mensaje = Mensaje(self, destinatario, contenido)
        destinatario.recibir_mensaje(mensaje)
        destinatario.recibir_notificacion(f"📩 Nuevo mensaje de {self.nombre}")
    
    def recibir_mensaje(self, mensaje):
        self.mensajes.append(mensaje)
    
    def recibir_notificacion(self, contenido):
        self.notificaciones.append(Notificacion(contenido))
    
    def mostrar_mensajes(self):
        for m in self.mensajes:
            print(m)
    
    def mostrar_notificaciones(self):
        for n in self.notificaciones:
            print(n)
    
    def puede_ver(self, otro_usuario):
        """Sistema de privacidad"""
        if otro_usuario.privacidad == "publico":
            return True
        elif otro_usuario.privacidad == "amigos" and self in otro_usuario.amigos:
            return True
        elif otro_usuario.privacidad == "privado" and self == otro_usuario:
            return True
        return False
    
    def __str__(self):
        return f"Usuario: {self.nombre} ({self.privacidad})"

# ------------------ FUNCIONALIDADES ------------------

class Grupo:
    def __init__(self, nombre, creador, privacidad="publico"):
        self.nombre = nombre
        self.creador = creador
        self.miembros = [creador]
        self.privacidad = privacidad
    
    def agregar_miembro(self, usuario):
        if usuario not in self.miembros:
            self.miembros.append(usuario)
            usuario.recibir_notificacion(f"Te uniste al grupo '{self.nombre}' 🎉")
    
    def publicar_mensaje(self, autor, contenido):
        if autor in self.miembros:
            for miembro in self.miembros:
                if miembro != autor:
                    miembro.recibir_notificacion(f"📢 Nuevo mensaje en {self.nombre} de {autor.nombre}: {contenido}")
        else:
            print("❌ No eres miembro de este grupo.")
    
    def __str__(self):
        return f"Grupo: {self.nombre} (Privacidad: {self.privacidad})"

class Evento:
    def __init__(self, titulo, fecha, creador):
        self.titulo = titulo
        self.fecha = fecha
        self.creador = creador
        self.participantes = [creador]
    
    def invitar(self, usuario):
        usuario.recibir_notificacion(f"📅 Invitación al evento '{self.titulo}' de {self.creador.nombre}")
    
    def confirmar_asistencia(self, usuario):
        if usuario not in self.participantes:
            self.participantes.append(usuario)
    
    def __str__(self):
        return f"Evento: {self.titulo} el {self.fecha} | Creador: {self.creador.nombre}"

class Mensaje:
    def __init__(self, remitente, destinatario, contenido):
        self.remitente = remitente
        self.destinatario = destinatario
        self.contenido = contenido
        self.fecha = datetime.now()
    
    def __str__(self):
        return f"[{self.fecha.strftime('%Y-%m-%d %H:%M')}] {self.remitente.nombre} → {self.destinatario.nombre}: {self.contenido}"

class Notificacion:
    def __init__(self, contenido):
        self.contenido = contenido
        self.fecha = datetime.now()
    
    def __str__(self):
        return f"🔔 {self.fecha.strftime('%Y-%m-%d %H:%M')} | {self.contenido}"


ana = Usuario("Ana", privacidad="publico")
luis = Usuario("Luis", privacidad="amigos")
sofia = Usuario("Sofía", privacidad="privado")

ana.agregar_amigo(luis)

ana.enviar_mensaje(luis, "Hola Luis, ¿cómo estás?")
luis.enviar_mensaje(ana, "Todo bien, ¿y tú?")

grupo1 = Grupo("Gamers", ana)
grupo1.agregar_miembro(luis)
grupo1.publicar_mensaje(ana, "Bienvenidos al grupo 🎮")

evento = Evento("Maratón de juegos", "2025-10-15", ana)
evento.invitar(luis)
evento.confirmar_asistencia(luis)

print("\n🔒 Privacidad:")
print("¿Ana puede ver a Sofía?", ana.puede_ver(sofia))
print("¿Luis puede ver a Ana?", luis.puede_ver(ana))

print("\n📩 Notificaciones de Luis:")
luis.mostrar_notificaciones()

print("\n📩 Mensajes de Ana:")
ana.mostrar_mensajes()
