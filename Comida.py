from Producto import Producto

class Comida(Producto):
    def __init__(self, nombre, subtotal, iva, total, tipo):
        super().__init__(nombre, subtotal, iva,total)
        self.tipo = tipo
        
    def mostrar(self):
        print(f"\n\tNombre: {self.nombre}\n\tTipo: {self.tipo}\n\tSubtotal: {self.subtotal}$\n\tIVA: {self.iva}$\n\tPrecio total: {self.total}$")
        