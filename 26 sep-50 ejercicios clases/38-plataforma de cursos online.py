class Leccion:
    def __init__(self, titulo):
        self.titulo = titulo
        self.completada = False

    def completar(self):
        self.completada = True
        print(f"✅ Lección '{self.titulo}' completada.")


class Modulo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lecciones = []

    def agregar_leccion(self, leccion):
        self.lecciones.append(leccion)

    def progreso(self):
        completadas = sum(1 for l in self.lecciones if l.completada)
        total = len(self.lecciones)
        return (completadas / total) * 100 if total > 0 else 0


class Curso:
    def __init__(self, titulo):
        self.titulo = titulo
        self.modulos = []

    def agregar_modulo(self, modulo):
        self.modulos.append(modulo)

    def progreso_total(self):
        if not self.modulos:
            return 0
        return sum(m.progreso() for m in self.modulos) / len(self.modulos)


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = {}

    def inscribir(self, curso):
        self.cursos[curso.titulo] = curso
        print(f"{self.nombre} se inscribió en el curso '{curso.titulo}'.")

    def progreso_curso(self, curso):
        progreso = curso.progreso_total()
        print(f"📊 Progreso de {self.nombre} en '{curso.titulo}': {progreso:.2f}%")
        if progreso == 100:
            print(f"🎉 {self.nombre} obtuvo la certificación en '{curso.titulo}'.")



curso1 = Curso("Programación en Python")


mod1 = Modulo("Introducción")
mod2 = Modulo("POO")


l1 = Leccion("Qué es Python")
l2 = Leccion("Variables y Tipos de datos")
l3 = Leccion("Clases y Objetos")
l4 = Leccion("Herencia")

mod1.agregar_leccion(l1)
mod1.agregar_leccion(l2)
mod2.agregar_leccion(l3)
mod2.agregar_leccion(l4)


curso1.agregar_modulo(mod1)
curso1.agregar_modulo(mod2)

est1 = Estudiante("Laura")


est1.inscribir(curso1)


l1.completar()
l2.completar()
l3.completar()
l4.completar()


est1.progreso_curso(curso1)
