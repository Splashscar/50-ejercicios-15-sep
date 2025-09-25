class usuario:
    def __init__(self, nombre, contraseña, cargo):
        self.nombre = nombre
        self.contraseña = contraseña
        self.cargo = cargo

class admin(usuario):
    def __init__(self, nombre, contraseña, cargo):
        super().__init__(nombre, contraseña, cargo)

    def permisos(self):
        return f"El usuario {self.nombre} tiene permisos de administrador."
permisos_admin = admin("Controlar ingresos y egresos", "Agregar nuevos usuarios", "Dar de baja usuarios")
print(permisos_admin.permisos())

    
class Cliente(usuario):
    def __init__(self, nombre, contraseña, cargo):
        super().__init__(nombre, contraseña, cargo)

    def permisos(self):
        return f"El usuario {self.nombre} tiene permisos de cliente."  
permisos_cliente = Cliente("Ver productos", "Realizar compras", "Dejar comentarios")
print(permisos_cliente.permisos())

class Moderador(usuario):
    def __init__(self, nombre, contraseña, cargo):
        super().__init__(nombre, contraseña, cargo)

    def permisos(self):
        return f"El usuario {self.nombre} tiene permisos de moderador."
permisos_moderador = Moderador("Gestionar comentarios", "Supervisar actividades", "Reportar usuarios")
print(permisos_moderador.permisos())

usuario1 = admin("adminUser", "adminPass", "Administrador")
usuario2 = Cliente("clientUser", "clientPass", "Cliente")
usuario3 = Moderador("modUser", "modPass", "Moderador")

print(f"Usuario: {usuario1.nombre}, Cargo: {usuario1.cargo}")
print(f"Usuario: {usuario2.nombre}, Cargo: {usuario2.cargo}")
print(f"Usuario: {usuario3.nombre}, Cargo: {usuario3.cargo}")

print(usuario1.permisos(), permisos_admin.permisos())
print(usuario2.permisos(), permisos_cliente.permisos())
print(usuario3.permisos(), permisos_moderador.permisos())
    
    