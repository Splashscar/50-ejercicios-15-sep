class Estudiante:
    def __init__(self, nombre, documento, programa):
        self.nombre = nombre
        self.documento = documento
        self.programa = programa

    def __str__(self):
        return f"Nombre: {self.nombre}, Documento: {self.documento}, Programa: {self.programa}"


estudiantes = {}

estudiantes["123456789"] = Estudiante("Felipe Mendieta", "123456789", "ADSO")
estudiantes["987654321"] = Estudiante("Maria Lopez", "987654321", "Contaduría")
estudiantes["456789123"] = Estudiante("Carlos Ruiz", "456789123", "Ingeniería")

for doc, est in estudiantes.items():
    print(est)

doc_buscar = "987654321"
if doc_buscar in estudiantes:
    print("\nEstudiante encontrado:")
    print(estudiantes[doc_buscar])
else:
    print("\nNo se encontró ese documento.")
