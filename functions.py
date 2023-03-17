from Piloto import Piloto
from Constructor import Constructor

"""Convertir las estructuras de datos en objetos"""
def carrera_objects(edd):
    carreras = []
    pass

"""id": "alfa",
    "name": "Alfa Romeo",
    "nationality": "Swiss"""
def constructores_objetos(edd,pilotos):
    pilots, constructores = [] , []
    for builder in edd:
        for piloto in pilotos:
            if piloto.team == builder['id']:
                pilots.append(piloto.id)
        x = Constructor(builder['id'],builder['name'],builder['nacionalidad'],pilots)

    
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
        