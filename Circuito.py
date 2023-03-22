class Circuito:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location
        
    def mostrar(self):
        return(f"CIRCUITO\nID: {self.id}\nName: {self.name}\n{self.location.mostrar()}")
        