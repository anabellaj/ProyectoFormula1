from Producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, subtotal, iva,total, alcoholico):
        super().__init__(nombre, subtotal,iva,total)
        self.alcoholico = alcoholico
        
    def mostrar(self):
        print(f"\n\tNombre: {self.nombre}\n\tSubtotal: {self.subtotal}$\n\tIVA: {self.iva}$\n\tPrecio total: {self.total}$")
        if self.alcoholico:
            print('\tBebida alcoholica')
        else:
            print('\tBebida no alcoholica')
            