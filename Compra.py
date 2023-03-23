class Compra:
    def __init__(self, cedula, orden, subtotal, descuento, total):
        self.cedula = cedula
        self.orden = orden
        self.subtotal = subtotal
        self.descuento = descuento
        self.total = total
        
    def mostrar(self):
        for k,v in self.orden.items():
            print(f"\tProducto: {k} - Cantidad: {v}")
        print(f"\tSubtotal: {self.subtotal}$\n\tDescuento: {self.descuento}$\n\tTotal: {self.total}$")
        