class Carrera:
    def __init__(self, ronda, nombre, circuito, fecha, restaurantes,podio,mapa,asistencia):
        self.ronda = ronda
        self.nombre = nombre
        self.fecha = fecha
        self.circuito = circuito
        self.restaurantes = restaurantes
        self.podio = podio
        self.mapa  = mapa
        self.asistencia = asistencia

    def mostrar(self):
        print(f"\nNombre: {self.nombre}\nFecha: {self.fecha}\n{self.circuito.mostrar()}")
        print('Restaurantes:')
        for r in self.restaurantes:
            print('\t',r)
        # if self.podio:
        #     print('\nPodio:',self.podio)
        
    def get_month(self):
        mes = self.fecha.split('-')
        return mes[1]
        
        
        
        