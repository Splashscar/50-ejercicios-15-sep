from datetime import datetime
import random

class Producto:
    def __init__(self, nombre, stock, precio):
        self.nombre = nombre
        self.stock = stock
        self.precio = precio
        self.historial_ventas = []  
    
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            self.historial_ventas.append(cantidad)
            print(f"✅ Venta: {cantidad} {self.nombre}. Stock actual: {self.stock}")
        else:
            print(f"❌ No hay suficiente stock de {self.nombre}")
    
    def predecir_stock(self):
        if not self.historial_ventas:
            return "No hay datos suficientes para predicción."
        promedio_ventas = sum(self.historial_ventas) / len(self.historial_ventas)
        dias_restantes = self.stock / promedio_ventas if promedio_ventas > 0 else float("inf")
        return f"📊 Se estima que el stock de {self.nombre} durará {dias_restantes:.1f} días (ventas promedio: {promedio_ventas:.1f}/día)."
    
    def __str__(self):
        return f"{self.nombre} | Stock: {self.stock} | Precio: ${self.precio}"


class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def surtir(self, producto, cantidad):
        producto.stock += cantidad
        print(f"🚚 {self.nombre} entregó {cantidad} unidades de {producto.nombre}. Stock actual: {producto.stock}")


class Orden:
    def __init__(self, producto, cantidad, proveedor):
        self.producto = producto
        self.cantidad = cantidad
        self.proveedor = proveedor
        self.fecha = datetime.now()
        self.estado = "Pendiente"
    
    def procesar(self):
        self.proveedor.surtir(self.producto, self.cantidad)
        self.estado = "Completada"
    
    def __str__(self):
        return f"Orden: {self.cantidad} {self.producto.nombre} a {self.proveedor.nombre} ({self.estado})"


class Almacen:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.ordenes = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def generar_orden(self, producto, cantidad, proveedor):
        orden = Orden(producto, cantidad, proveedor)
        self.ordenes.append(orden)
        print(f"📦 Generada {orden}")
        return orden
    
    def mostrar_stock(self):
        print(f"--- Stock en {self.nombre} ---")
        for p in self.productos:
            print(p)



p1 = Producto("Arroz", 50, 2.5)
p2 = Producto("Aceite", 30, 5.0)

prov = Proveedor("Proveedor Central")

almacen = Almacen("Almacén Principal")
almacen.agregar_producto(p1)
almacen.agregar_producto(p2)

for _ in range(5):
    p1.vender(random.randint(5, 10)) 
    p2.vender(random.randint(1, 5))

print("\n--- Predicción de Stock ---")
print(p1.predecir_stock())
print(p2.predecir_stock())

orden1 = almacen.generar_orden(p1, 40, prov)
orden1.procesar()

print("\n--- Stock Final ---")
almacen.mostrar_stock()
