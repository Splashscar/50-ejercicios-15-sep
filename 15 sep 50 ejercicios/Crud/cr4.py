class CRUD:
    def __init__(self, archivo):
        self.archivo = archivo

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
    opcion = input("Seleccione acción: eliminar o salir: ").lower()
    if opcion == "eliminar":
        crud_empresa.eliminar()
    elif opcion == "salir":
        break
    else:
        print("Opción no válida.")
    print("-----------------")