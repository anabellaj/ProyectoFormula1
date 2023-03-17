class Constructor:
    def __init__(self, id, nombre, nacionalidad, pilotos):
        self.id = id
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.pilotos = pilotos
        
        
    def mostrar(self):
        print(self.id,self.nombre,self.nacionalidad,self.pilotos)