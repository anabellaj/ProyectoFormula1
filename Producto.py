class Producto:
    def __init__(self, nombre, inventario, subtotal, iva, total):
        self.nombre = nombre
        self.subtotal = subtotal
        self.iva = iva
        self.total = total
        self.inventario = inventario
        
    def mostrar(self):
        pass