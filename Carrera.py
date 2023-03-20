
class Carrera:
    def __init__(self, ronda, nombre, circuito, fecha, restaurantes):
        self.ronda = ronda
        self.nombre = nombre
        self.fecha = fecha
        self.circuito = circuito
        self.restaurantes = restaurantes

    def mostrar(self):
        print(self.ronda, self.nombre,self.circuito.mostrar(),self.fecha)
        for r in self.restaurantes:
            r.mostrar()
    
        
        
        