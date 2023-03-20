from Producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, alcoholico):
        super().__init__(nombre, precio)
        self.alcoholico = alcoholico
        
        