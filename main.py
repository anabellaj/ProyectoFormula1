import requests
from functions import *

carrera_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json')
pilotos_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json')
constructores_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json')

def main():
    carreras_edd = carrera_url.json()
    pilotos_edd = pilotos_url.json()
    constructores_edd = constructores_url.json()
    pilotos = pilotos_objetos(pilotos_edd)
    constructores = constructores_objetos(constructores_edd, pilotos)
    constructores = constructores_objetos(constructores_edd, pilotos)
    circuitos = circuito_obj(carreras_edd)
    carreras = carrera_objects(carreras_edd, circuitos)
    restaurantes, productos = restaurantes_obj(carreras_edd)
    codigos, clientes = [], []
    
    while True:
        opt = get_option()
        
        #1: Gestion de carreras y equipos
        if opt == 1:
            print('\nUsted ha ingresado a la gestion de carrera y equipos!')
            opti = input('\nPresione 1 para buscar constructores por pais\nPresione 2 para ver los pilotos de cada constructor\nPresione 3 para buscar las carreras por pais del circuito\nPresione 4 para buscar todas las carreras en un mes especifico\nPresione 5 para terminar una carrera y obtener su podio\n\n>> ')
            while not opti.isnumeric() or int(opti) not in range(1,6):
                opti = input('\nERROR - Opcion Invalida\nPresione 1 para buscar constructores por pais\nPresione 2 para ver los pilotos de cada constructor\nPresione 3 para buscar las carreras por pais del circuito\nPresione 4 para buscar todas las carreras en un mes especifico\nPresione 5 para terminar una carrera y obtener su podio\n\n>> ')
            if opti == '1':
                print('\n------ BUSQUEDA DE CONSTRUCTORES POR PAIS ------')
                filter_paises(constructores)
            elif opti == '2':
                print('\n----- BUSQUEDA DE PILOTOS POR CONSTRUCTOR -----')
                filter_pilots(constructores)
            elif opti =='3':
                print('\n----- BUSQUEDA DE CARRERAS POR PAIS -----')
                filter_carreras(carreras,circuitos)
            elif opti == '4':
                print('\n----- BUSQUEDA DE CARRERAS POR MES -----')
                filter_months(carreras)
            elif opti =='5':
                pilotos, constructores,carreras = get_podio(pilotos, carreras, constructores)
                                      
        #2: Gestion de venta de entradas
        elif opt == 2:
            print('\nUsted ha ingresado a la gestion de venta de entradas!')
            clientes, carreras, codigos = get_client_data(carreras, codigos)
            
            # mapa = carreras[20].mapa
            # print(carreras[20].nombre)
            # imprimir_mapa(mapa)
            
        #3: Gestion de asistencia a las carreras
        elif opt == 3:
            print('\nUsted ha ingresado a la gestion de asistencia a las carreras!')
            opti = input('\nPresione 1 para validar un ticket\nPresione 2 para chequear la asistencia para una carrera\n>> ')
            while not opti.isnumeric() or int(opti) not in range(1,3):
                opti = input('\nERROR - Ingreso Invalido\nPresione 1 para validar un ticket\nPresione 2 para chequear la asistencia para una carrera\n>> ')
            if opti == '1':
                print('\n----- VALIDACION DE TICKETS -----')
                carreras, codigos = confirmar_asistencia(clientes, codigos, carreras)
            elif opti == '2':
                print('\n----- CHEQUEO DE ASISTENCIA -----')
                chequear_asistencia(carreras)
            
        #4: Gestion de restaurantes
        elif opt == 4:
            print('\nUsted ha ingresado a la gestion de restaurantes!')
            opti = input('\nPresione 1 para buscar productos por su nombre\nPresione 2 para buscar productos en un rango de precio\nPresione 3 para buscar productos por tipo\n>> ')
            while not opti.isnumeric() or int(opti) not in range(1,4):
                opti = input('\nERROR - Ingreso Invalido\nPresione 1 para buscar productos por su nombre\nPresione 2 para buscar productos en un rango de precio\nPresione 3 para buscar productos por tipo\n>> ')
            if opti == '1':
                pass
            elif opti == '2':
                pass
            elif opti == '3':
                productos_precio(productos)
            
        #5: Gestion de venta de restaurantes 
        elif opt == 5:
            print('\nUsted ha ingresado a la gestion de venta de restaurantes!')
            pass
        
        #6: Estadisticas
        elif opt == 6:
            print('\nUsted ha ingresado a la seccion de estadisticas!')
            pass
        
        #7: Salir
        else: 
            print('\nHasta pronto! ⚙️\n\n')
            break
    
    
    
main()
