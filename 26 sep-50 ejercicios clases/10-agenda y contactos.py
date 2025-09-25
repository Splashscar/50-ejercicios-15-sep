class contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"
    
class agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def mostrar_contactos(self):
        for contacto in self.contactos:
            print(contacto)

mi_agenda = agenda()
while True:
    print("\nSeleccione una opción:")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Salir")
    opcion = input("Ingrese la opción (1/2/3): ")
    
    if opcion == '1':
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        nuevo_contacto = contacto(nombre, telefono, email)
        mi_agenda.agregar_contacto(nuevo_contacto)
        print(f"Contacto '{nombre}' agregado.")
        
    elif opcion == '2':
        print("Contactos en la agenda:")
        mi_agenda.mostrar_contactos()
        
    elif opcion == '3':
        print("Gracias por usar la agenda de contactos.")
        break
        
    else:
        print("Opción inválida. Intente de nuevo.")