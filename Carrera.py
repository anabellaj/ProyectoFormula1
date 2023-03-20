
class Carrera:
    def __init__(self, ronda, nombre, circuito, fecha):
        self.ronda = ronda
        self.nombre = nombre
        self.fecha = fecha
        self.circuito = circuito

    def mostrar(self):
        print(self.ronda, self.nombre,self.circuito.mostrar(),self.fecha)
        
    
        
        
        