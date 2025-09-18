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

crud_empresa = CRUD("personal.txt")

while True:
    opcion = input("Seleccione acción: crear o salir: ").lower()
    if opcion == "crear":
        crud_empresa.crear()
    elif opcion == "salir":
        break
    else:
        print("Opción no válida.")
    print("-----------------")