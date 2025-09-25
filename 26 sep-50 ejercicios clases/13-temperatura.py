class temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def from_fahrenheit(self, fahrenheit):
        self.celsius = (fahrenheit - 32) * 5/9
        return self.celsius

    def from_kelvin(self, kelvin):
        self.celsius = kelvin - 273.15
        return self.celsius
    
temp = input("Ingrese la temperatura en Celsius: ")
temp = temperatura(float(temp))
print("Que conversion te gustaria hacer?: ")
print("1. Celsius a Fahrenheit")
print("2. Celsius a Kelvin")
opcion = input("Ingrese la opcion (1/2): ")
if opcion == '1':
    print(f"{temp.celsius}°C son {temp.to_fahrenheit()}°F")
elif opcion == '2':
    print(f"{temp.celsius}°C son {temp.to_kelvin()}K")