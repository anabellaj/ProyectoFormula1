import requests
carrera_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json')
from Restaurante import Restaurante
from Bebida import Bebida
from Comida import Comida

def main():
    carrera_edd = carrera_url.json()
    def restaurantes_obj(edd):
        restaurantes = []
        for carrera in edd:
            for restaur in carrera['restaurants']:
                items = restaur['items']
                for i in items:   
                    prod = []
                    prod_type = i['type'].split(':')
                    if prod_type[0] == 'drink':
                        if prod_type[1] == 'alcoholic':
                            y = Bebida(items['name'], items['price'], True)
                            prod.append(y)
                        else:
                            y = Bebida(items['name'], items['price'], False)
                            prod.append(y)
                    if prod_type[0] == 'food':
                        y =Comida(items['name'], items['price'],prod_type[1])
                        prod.append(y)
                x = Restaurante(restaur['name'],prod)
                restaurantes.append(x)
        return restaurantes
    input('go')
    r = restaurantes_obj(carrera_edd)
    for t in r:
        t.mostrar()
main()