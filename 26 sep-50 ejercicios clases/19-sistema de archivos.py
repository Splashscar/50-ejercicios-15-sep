class ElementoSistema:
    def __init__(self, nombre):
        self.nombre = nombre

    def obtener_nombre(self):
        return self.nombre
    
class Archivo(ElementoSistema):
    def __init__(self, nombre, tamano):
        super().__init__(nombre)
        self.tamano = tamano  

    def obtener_tamano(self):
        return self.tamano
    
class Carpeta(ElementoSistema):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.contenido = [] 

    def agregar_elemento(self, elemento):
        self.contenido.append(elemento)

    def listar_contenido(self):
        for elem in self.contenido:
            if isinstance(elem, Archivo):
                print(f"Archivo: {elem.obtener_nombre()}, Tamaño: {elem.obtener_tamano()} bytes")
            elif isinstance(elem, Carpeta):
                print(f"Carpeta: {elem.obtener_nombre()}")


raiz = Carpeta("raiz")
documentos = Carpeta("Documentos")
imagenes = Carpeta("Imágenes")
archivo1 = Archivo("archivo1.txt", 1200)
archivo2 = Archivo("foto.jpg", 250000)
archivo3 = Archivo("presentacion.pptx", 45000)
documentos.agregar_elemento(archivo1)
imagenes.agregar_elemento(archivo2)
raiz.agregar_elemento(documentos)
raiz.agregar_elemento(imagenes)
raiz.agregar_elemento(archivo3)
print("Contenido de la carpeta raíz:")
raiz.listar_contenido()
print("\nContenido de la carpeta Documentos:")
documentos.listar_contenido()
print("\nContenido de la carpeta Imágenes:")
imagenes.listar_contenido()
