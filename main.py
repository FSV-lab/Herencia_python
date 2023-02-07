
class Vehiculo:
    Color='Rojo'
    Ruedas = None
    Puertas = None

    def Velocidad(self):
        print('Este Vehiculo va a una  Velocidad de 197 km por hora')
    
    def Cilindrada(self):
        print('El  Vehiculo tiene un Cilindraje de 2,0')
        
class Coche(Vehiculo):
    def info(self): 
        pass

    
c = Coche()
c.Cilindrada()
c.Velocidad()
print(c.Cilindrada,'y su',c.Velocidad)

