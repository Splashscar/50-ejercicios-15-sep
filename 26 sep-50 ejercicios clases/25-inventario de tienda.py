class Categoria:
    def __init__(self, nombre, descripcion=""):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"Categoría: {self.nombre} - {self.descripcion}"


class Producto:
    def __init__(self, nombre, precio, cantidad, categoria: Categoria):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} ({self.categoria.nombre}) - ${self.precio} - Stock: {self.cantidad}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        return resultados

    def buscar_por_categoria(self, categoria_nombre):
        resultados = [p for p in self.productos if p.categoria.nombre.lower() == categoria_nombre.lower()]
        return resultados

    def reporte_stock(self):
        print("\n📦 Reporte de Inventario 📦")
        for p in self.productos:
            estado = "✅ Suficiente" if p.cantidad > 5 else "⚠️ Bajo stock"
            print(f"{p.nombre} - Stock: {p.cantidad} ({estado})")

electronica = Categoria("Electrónica", "Dispositivos y gadgets")
ropa = Categoria("Ropa", "Prendas de vestir")

p1 = Producto("Laptop", 3500, 10, electronica)
p2 = Producto("Camiseta", 50, 3, ropa)
p3 = Producto("Auriculares", 150, 7, electronica)

inv = Inventario()
inv.agregar_producto(p1)
inv.agregar_producto(p2)
inv.agregar_producto(p3)

print("\n🔍 Búsqueda por nombre 'lap':")
for r in inv.buscar_por_nombre("lap"):
    print(r)

print("\n🔍 Búsqueda por categoría 'Electrónica':")
for r in inv.buscar_por_categoria("Electrónica"):
    print(r)

inv.reporte_stock()

