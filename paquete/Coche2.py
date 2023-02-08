from Vehiculo import *

class Coche(vehiculo):
    def __init__(self,Color,Ruedas,Puertas):
        self.Color= Color
        self.Ruedas=Ruedas
        self.Puertas=Puertas
        
    def datos_vehiculo(self):
        print(f"El  color de su Coche es: {self.Color} y tiene {self.Ruedas} ruedas con {self.Puertas} puertas")  
    
coche1=Coche("Rojo", 4, 4)
coche1.datos_vehiculo()
coche1.Cilindraje()
coche1.Velocidad()