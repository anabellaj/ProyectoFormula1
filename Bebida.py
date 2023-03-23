from Producto import Producto

class Bebida(Producto):       
    def __init__(self, nombre, inventario, subtotal, iva, total,alcoholico):
        super().__init__(nombre, inventario, subtotal, iva, total)
        self.alcoholico =  alcoholico
        
    def mostrar(self):
        print(f"\nNombre: {self.nombre}\n\tCantidad disponible: {self.inventario}\n\tSubtotal: {self.subtotal}$\n\tIVA: {self.iva}$\n\tPrecio total: {self.total}$")
        if self.alcoholico:
            print('\tBebida alcoholica')
        else:
            print('\tBebida no alcoholica')
            