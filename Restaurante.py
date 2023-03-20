class Restaurante:
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos
        
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print('Productos')
        for p in self.productos:
            p.mostrar()
        