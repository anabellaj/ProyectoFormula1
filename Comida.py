from Producto import Producto

class Comida(Producto):
    def __init__(self, nombre, inventario, subtotal, iva, total,tipo):
        super().__init__(nombre, inventario, subtotal, iva, total)
        self.tipo =  tipo
        
    def mostrar(self):
        print(f"\nNombre: {self.nombre}\n\tTipo: {self.tipo}\n\tCantidad disponible: {self.inventario}\n\tSubtotal: {self.subtotal}$\n\tIVA: {self.iva}$\n\tPrecio total: {self.total}$")
        