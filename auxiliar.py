import requests
carrera_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json')
from Restaurante import Restaurante
from Bebida import Bebida
from Comida import Comida

refresco = Bebida('pepsi',300,45,45*0.16,45*1.16,False)
refresco.mostrar()
r = refresco
r.alcoholico = True
refresco.mostrar()
r.mostrar()
