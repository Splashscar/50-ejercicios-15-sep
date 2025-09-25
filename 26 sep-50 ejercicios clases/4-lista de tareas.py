class ListaTareas:
    def __init__ (self):
        self.tareas = []
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada.")
    def eliminar_tarea(self, tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            print(f"Tarea '{tarea}' eliminada.")
        else:
            print(f"Tarea '{tarea}' no encontrada.")
    def marcar_como_completada(self, tarea):
        if tarea in self.tareas:
            print(f"Tarea '{tarea}' marcada como completada.")
        else:
            print(f"Tarea '{tarea}' no encontrada.")
    def mostrar_tareas(self):
        if self.tareas:
            print("Lista de tareas:")
            for idx, tarea in enumerate(self.tareas, 1):
                print(f"{idx}. {tarea}")
        else:
            print("No hay tareas en la lista.")

lista = ListaTareas()
while True:
    print("\nSeleccione una opcion:")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Marcar tarea como completada")
    print("4. Mostrar tareas")
    print("5. Salir")
    opcion = input("Ingrese la opcion (1/2/3/4/5): ")
    if opcion == '1':
        tarea = input("Ingrese la descripcion de la tarea: ")
        lista.agregar_tarea(tarea)
    elif opcion == '2':
        tarea = input("Ingrese la descripcion de la tarea a eliminar: ")
        lista.eliminar_tarea(tarea)
    elif opcion == '3':
        tarea = input("Ingrese la descripcion de la tarea a marcar como completada: ")
        lista.marcar_como_completada(tarea)
    elif opcion == '4':
        lista.mostrar_tareas()
    elif opcion == '5':
        print("Gracias por usar el gestor de tareas.")
        break
    else:
        print("Opcion invalida. Intente de nuevo.")