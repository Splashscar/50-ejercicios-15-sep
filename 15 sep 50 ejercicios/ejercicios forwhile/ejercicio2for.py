class comida:
 def __init__(self, platos, texturas, cogcion):
                 self.platos = platos
                 self.texturas = texturas
                 self.cogcion = cogcion
comidas = comida("carnes", "pollos", "ensaladas" )
print(comidas.platos, comidas.texturas, comidas.cogcion)
menu = ["hamburguesa","pizza","arepa","suchi"]
print("menu del dia:")
for comida in menu:
        print("chef",comida)