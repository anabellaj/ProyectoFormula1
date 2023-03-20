from Producto import Producto

class Comida(Producto):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo
        
    def mostrar(self):
        print(f"\n\tNombre: {self.nombre}\n\tPrecio: {self.precio}\n\tTipo: {self.tipo}")
        