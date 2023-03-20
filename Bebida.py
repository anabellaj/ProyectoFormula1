from Producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, alcoholico):
        super().__init__(nombre, precio)
        self.alcoholico = alcoholico
        
    def mostrar(self):
        print(f"\n\tNombre: {self.nombre}\n\tPrecio: {self.precio}")
        if self.alcoholico:
            print('Bebida alcoholica')
        else:
            print('Bebida no alcoholica')
            