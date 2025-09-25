class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.seguidos = []
        self.publicaciones = []

    def seguir(self, otro_usuario):
        if otro_usuario not in self.seguidos and otro_usuario != self:
            self.seguidos.append(otro_usuario)
            print(self.nombre, "ahora sigue a", otro_usuario.nombre)

    def publicar(self, texto):
        pub = Publicacion(self, texto)
        self.publicaciones.append(pub)
        return pub


class Publicacion:
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto
        self.likes = 0
        self.comentarios = []

    def dar_like(self):
        self.likes += 1

    def comentar(self, usuario, texto):
        com = Comentario(usuario, texto)
        self.comentarios.append(com)
        return com

    def mostrar(self):
        print(f"\n{self.autor.nombre} publicó: {self.texto}")
        print(f"👍 {self.likes} likes | 💬 {len(self.comentarios)} comentarios")
        for c in self.comentarios:
            print("-", c.usuario.nombre, ":", c.texto)


class Comentario:
    def __init__(self, usuario, texto):
        self.usuario = usuario
        self.texto = texto


u1 = Usuario("Ana")
u2 = Usuario("Luis")


u1.seguir(u2)


pub1 = u2.publicar("Hola, este es mi primer post! 😎")


pub1.dar_like()
pub1.dar_like()
pub1.comentar(u1, "¡Qué bacano tu post!")
pub1.comentar(u1, "Publica más seguido 🔥")


pub1.mostrar()
