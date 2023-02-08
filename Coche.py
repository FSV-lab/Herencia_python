
class Vehiculo():
    Color = None
    Ruedas = None
    Puertas = None    
        
    def Velocidad(self):
        print('Este Vehiculo va a una  Velocidad de 197 km por hora')
    
    def Cilindrada(self):
        print('El  Vehiculo tiene un Cilindraje de 2,0')
        
class Coche(Vehiculo):
      
    def info(self): 
        print('El Coche es de Color:',Color,'Tiene',Puertas,'puertas','y consta de ',Ruedas,'ruedas.')
  
c = Coche()
c.Cilindrada()
c.Velocidad()
print(c.Cilindrada,c.Velocidad)


