class Ubicacion:
    def __init__(self, latitud, longitud, ciudad, pais):
        self.latitud = latitud
        self.longitud = longitud
        self.ciudad = ciudad
        self.pais = pais
        
    def mostrar(self):
        return (f"UBICACION:\n\tLatitud: {self.latitud}\n\tLongitud: {self.longitud}\n\tCiudad: {self.ciudad}\n\tPais: {self.pais}")