from Producto import Producto

class Comida(Producto):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo
        
        