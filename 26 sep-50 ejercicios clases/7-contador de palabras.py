class contadorTexto:
    def __init__(self, texto):
        self.texto = texto

    def contar_palabras(self):
        palabras = self.texto.split()
        return len(palabras)
    def contar_caracteres(self):
        return len(self.texto)
    def contar_lineas(self):
        lineas = self.texto.splitlines()
        return len(lineas)
    
texto = input("Ingrese un texto: ")
contador = contadorTexto(texto)

print("El texto tiene:")
print(f"{contador.contar_palabras()} palabras")
print(f"{contador.contar_caracteres()} caracteres")
print(f"{contador.contar_lineas()} lineas")