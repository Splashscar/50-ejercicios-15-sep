class CRUD:
    def __init__(self, archivo):
        self.archivo = archivo

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

crud_empresa = CRUD("personal.txt")

while True:
    opcion = input("Seleccione acción: leer o salir: ").lower()
    if opcion == "leer":
        crud_empresa.leer()
    elif opcion == "salir":
        break
    else:
        print("Opción no válida.")
    print("-----------------")