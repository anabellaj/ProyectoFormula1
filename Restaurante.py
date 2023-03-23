class Restaurante:
    def __init__(self, nombre, productos,carrera):
        self.nombre = nombre
        self.productos = productos
        self.carrera = carrera
        
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print('Productos')
        for p in self.productos:
            p.mostrar()
        