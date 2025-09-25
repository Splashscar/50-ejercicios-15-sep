class Paquete:
    def __init__(self, codigo, peso, destino):
        self.codigo = codigo
        self.peso = peso
        self.destino = destino
        self.entregado = False

    def __str__(self):
        return f"📦 Paquete {self.codigo} ({self.peso}kg) → {self.destino}"


class Vehiculo:
    def __init__(self, placa, capacidad):
        self.placa = placa
        self.capacidad = capacidad  # en kg
        self.carga_actual = 0
        self.paquetes = []

    def asignar_paquete(self, paquete):
        if self.carga_actual + paquete.peso <= self.capacidad:
            self.paquetes.append(paquete)
            self.carga_actual += paquete.peso
            print(f"✅ Paquete {paquete.codigo} asignado al vehículo {self.placa}.")
            return True
        else:
            print(f"⚠️ Vehículo {self.placa} no tiene capacidad para el paquete {paquete.codigo}.")
            return False

    def entregar(self):
        for paquete in self.paquetes:
            paquete.entregado = True
            print(f"🚚 Entregado {paquete}")
        self.paquetes.clear()
        self.carga_actual = 0


class Ruta:
    def __init__(self, origen, destino, distancia):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia  # km

    def __str__(self):
        return f"Ruta {self.origen} → {self.destino} ({self.distancia} km)"


class Almacen:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.paquetes = []

    def recibir_paquete(self, paquete):
        self.paquetes.append(paquete)
        print(f"📥 {self.nombre} recibió {paquete}")

    def optimizar_entregas(self, vehiculos, rutas):
        """Asigna paquetes al vehículo más apto según capacidad y ruta más corta."""
        for paquete in self.paquetes:
            rutas_disponibles = [r for r in rutas if r.destino == paquete.destino]
            if not rutas_disponibles:
                print(f"❌ No hay ruta para {paquete.destino}.")
                continue

            ruta = min(rutas_disponibles, key=lambda r: r.distancia)

        
            vehiculos_aptos = [v for v in vehiculos if v.carga_actual + paquete.peso <= v.capacidad]
            if vehiculos_aptos:
                vehiculo = min(vehiculos_aptos, key=lambda v: v.carga_actual) 
                vehiculo.asignar_paquete(paquete)
            else:
                print(f"❌ Ningún vehículo disponible para {paquete.codigo}.")


        for v in vehiculos:
            if v.paquetes:
                print(f"\n🚦 Vehículo {v.placa} inicia ruta con {len(v.paquetes)} paquetes.")
                v.entregar()


almacen = Almacen("Central", "Bogotá")

p1 = Paquete("P001", 10, "Medellín")
p2 = Paquete("P002", 15, "Cali")
p3 = Paquete("P003", 20, "Medellín")

almacen.recibir_paquete(p1)
almacen.recibir_paquete(p2)
almacen.recibir_paquete(p3)

v1 = Vehiculo("ABC123", 25)
v2 = Vehiculo("XYZ789", 30)

r1 = Ruta("Bogotá", "Medellín", 400)
r2 = Ruta("Bogotá", "Cali", 450)

almacen.optimizar_entregas([v1, v2], [r1, r2])
