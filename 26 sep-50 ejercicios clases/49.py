import random

class Neurona:
    def __init__(self, n_entradas):
       
        self.pesos = [random.uniform(-1, 1) for _ in range(n_entradas)]
        self.bias = random.uniform(-1, 1)

    def activar(self, entradas):
       
        z = sum(e * p for e, p in zip(entradas, self.pesos)) + self.bias
        return 1 if z >= 0 else 0


class Red:
    def __init__(self, n_entradas):
        self.neurona = Neurona(n_entradas)

    def predecir(self, entradas):
        return self.neurona.activar(entradas)


class Entrenamiento:
    def __init__(self, red, tasa_aprendizaje=0.1):
        self.red = red
        self.tasa = tasa_aprendizaje

    def entrenar(self, datos, epocas=10):
        """
        datos: lista de (entradas, salida_esperada)
        """
        for e in range(epocas):
            print(f"\n📚 Época {e+1}")
            for entradas, esperado in datos:
                pred = self.red.predecir(entradas)
                error = esperado - pred

                
                for i in range(len(self.red.neurona.pesos)):
                    self.red.neurona.pesos[i] += self.tasa * error * entradas[i]
                self.red.neurona.bias += self.tasa * error

                print(f"Entradas: {entradas}, Esperado: {esperado}, "
                      f"Pred: {pred}, Error: {error}")


class Prediccion:
    def __init__(self, red):
        self.red = red

    def evaluar(self, entradas):
        resultado = self.red.predecir(entradas)
        print(f"🔮 Predicción para {entradas} → {resultado}")
        return resultado


datos_entrenamiento = [
    ([0, 0], 0),
    ([0, 1], 0),
    ([1, 0], 0),
    ([1, 1], 1)
]

red = Red(2)

trainer = Entrenamiento(red, tasa_aprendizaje=0.2)
trainer.entrenar(datos_entrenamiento, epocas=10)

predictor = Prediccion(red)
predictor.evaluar([0, 0])
predictor.evaluar([0, 1])
predictor.evaluar([1, 0])
predictor.evaluar([1, 1])
