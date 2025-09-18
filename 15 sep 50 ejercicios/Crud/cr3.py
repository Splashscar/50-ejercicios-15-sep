class CRUD:
    def __init__(self, archivo):
        self.archivo = archivo

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

crud_empresa = CRUD("personal.txt")

while True:
    opcion = input("Seleccione acción: actualizar o salir: ").lower()
    if opcion == "actualizar":
        crud_empresa.actualizar()
    elif opcion == "salir":
        break
    else:
        print("Opción no válida.")
    print("-----------------")