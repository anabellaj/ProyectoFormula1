class Constructor:
    def __init__(self, id, nombre, nacionalidad, pilotos, score):
        self.id = id
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.pilotos = pilotos
        self.score = score
        
    def mostrar(self):
        print(self.id,self.nombre,self.nacionalidad,self.pilotos, self.score)