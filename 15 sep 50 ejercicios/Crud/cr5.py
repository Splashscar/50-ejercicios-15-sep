class CRUD:
    def __init__(self, archivo):
        self.archivo = archivo

    def crear(self):
        nombre = input("Ingrese el nombre del empleado: ")
        cargo = input("Ingrese el cargo: ")
        edad = int(input("Ingrese la edad: "))
        with open(self.archivo, "a") as archivo:
            archivo.write(f"{nombre},{cargo},{edad}\n")
        print("Empleado guardado en el archivo.")

    def leer(self):
        try:
            with open(self.archivo, "r") as archivo:
                lineas = archivo.readlines()
                if not lineas:
                    print("No hay personal registrado.")
                for linea in lineas:
                    datos = linea.strip().split(",")
                    print(f"Nombre: {datos[0]}, Cargo: {datos[1]}, Edad: {datos[2]}")
        except FileNotFoundError:
            print("El archivo no existe.")

    def actualizar(self):
        nombre_buscar = input("Ingrese el nombre del empleado a actualizar: ")
        actualizado = False
        try:
            with open(self.archivo, "r") as archivo:
                lineas = archivo.readlines()
            with open(self.archivo, "w") as archivo:
                for linea in lineas:
                    datos = linea.strip().split(",")
                    if datos[0].lower() == nombre_buscar.lower():
                        nuevo_nombre = input("Nuevo nombre: ")
                        nuevo_cargo = input("Nuevo cargo: ")
                        nueva_edad = int(input("Nueva edad: "))
                        archivo.write(f"{nuevo_nombre},{nuevo_cargo},{nueva_edad}\n")
                        actualizado = True
                    else:
                        archivo.write(linea)
            if actualizado:
                print("Empleado actualizado.")
            else:
                print("Empleado no encontrado.")
        except FileNotFoundError:
            print("El archivo no existe.")

    def eliminar(self):
        nombre_eliminar = input("Ingrese el nombre del empleado a eliminar: ")
        eliminado = False
        try:
            with open(self.archivo, "r") as archivo:
                lineas = archivo.readlines()
            with open(self.archivo, "w") as archivo:
                for linea in lineas:
                    datos = linea.strip().split(",")
                    if datos[0].lower() != nombre_eliminar.lower():
                        archivo.write(linea)
                    else:
                        eliminado = True
            if eliminado:
                print("Empleado eliminado.")
            else:
                print("Empleado no encontrado.")
        except FileNotFoundError:
            print("El archivo no existe.")


crud_empresa = CRUD("personal.txt")

while True:
    opcion = input("Seleccione acción: crear, leer, actualizar, eliminar, salir: ").lower()
    if opcion == "crear":
        crud_empresa.crear()
    elif opcion == "leer":
        crud_empresa.leer()
    elif opcion == "actualizar":
        crud_empresa.actualizar()
    elif opcion == "eliminar":
        crud_empresa.eliminar()
    elif opcion == "salir":
        break
    else:
        print("Opción no válida.")
    print("-----------------")