from Piloto import Piloto
from Constructor import Constructor
from Bebida import Bebida
from Carrera import Carrera
from Circuito import Circuito
from Comida import Comida
from Producto import Producto
from Restaurante import Restaurante
from Ubicacion import Ubicacion

"""Convertir las estructuras de datos en objetos"""
def carrera_objects(edd, circuitos):
    carreras = []
    contador = 0
    for carrera in edd:
        circ = circuitos[contador]
        rest = []
        for res in carrera['restaurants']:
            rest.append(res['name'])
        x = Carrera(carrera['round'],carrera['name'],circ, carrera['date'], rest)
        carreras.append(x)
        contador+=1
    return carreras

def circuito_obj(edd):
    circuitos=[]
    for carrera in edd:
        loc = Ubicacion(carrera['circuit']['location']['lat'],carrera['circuit']['location']['long'],carrera['circuit']['location']['locality'],carrera['circuit']['location']['country'])
        x = Circuito(carrera['circuit']['circuitId'], carrera['circuit']['name'],loc)
        circuitos.append(x)
    return circuitos

def restaurantes_obj(edd):
    restaurantes = []
    for carrera in edd:
        for restaur in carrera['restaurants']:
            items = restaur['items']
            prod = []
            for i in items:   
                # prod = []
                prod_type = i['type'].split(':')
                if prod_type[0] == 'drink':
                    if prod_type[1] == 'alcoholic':
                        y = Bebida(i['name'], i['price'], True)
                        prod.append(y)
                    else:
                        y = Bebida(i['name'], i['price'], False)
                        prod.append(y)
                if prod_type[0] == 'food':
                    y =Comida(i['name'], i['price'],prod_type[1])
                    prod.append(y)
            x = Restaurante(restaur['name'],prod)
            restaurantes.append(x)
    return restaurantes

def constructores_objetos(edd,pilotos):
    pilots, constructores = [] , []
    for builder in edd:
        pilots = []
        for piloto in pilotos:
            if piloto.team == builder['id']:
                pilots.append(piloto.id)
        x = Constructor(builder['id'],builder['name'],builder['nationality'],pilots)
        constructores.append(x)
    return constructores
    
def pilotos_objetos(edd):
    pilotos = []
    for pilot in edd:
        x = Piloto(pilot['id'], pilot['permanentNumber'],pilot['code'],pilot['team'],pilot['firstName'],pilot['lastName'],pilot['dateOfBirth'],pilot['nationality'])
        pilotos.append(x)
    return pilotos
            

"""Seleccionar opcion""" 
def get_option():
    print('⚙️  Bienvenido al programa de Formula 1 ⚙️')
    while True:
        try:
            opt = int(input('\nPresione 1 para ingresar a la gestion de carreras y equipos\nPresione 2 para ingresar a la gestion de venta de entradas\nPresione 3 para ingresar a la gestion de asistencia a las carreras\npresione 4 para ingresar a la gestion de restaurantes\nPresione 5 para ingresar a la gestion de venta de restaurantes\nPresione 6 para visualizar las estadisticas\nPresione 7 para salir\n\nIndique el numero correspondiente a su eleccion: '))
            if opt not in range (1,8):
                raise Exception
            break
        except:
            print('\nERROR - Por favor ingrese una opcion valida')
    return opt

# def crear_mapa(filas,columnas):
#     mapa = []
#     for y in range(filas):
#         aux = []
#         for x in range(columnas):
#             aux.append(False)
#         mapa.append(aux)
#     return mapa 

# def imprimir_mapa(mapa):
#     print('*'*len(mapa(1)) + 'ESTADIO'+'*'*len(mapa(1)))
#     print('\n')
#     nums = '    '
#     for i, x in enumerate(mapa[1]):
#         if i > 8 :
#             nums += str(i+1)+'|'
#         else:
#             nums += str(i+1)+'|'
#     print(nums)
#     for i, x in enumerate(mapa):
        