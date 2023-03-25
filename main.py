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
    codigos, clientes, compras = [], [], []
    
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
            try:
                clientes, carreras, codigos = get_client_data(clientes, carreras, codigos)
            except:
                print('Compra cancelada')
            
        #3: Gestion de asistencia a las carreras
        elif opt == 3:
            print('\nUsted ha ingresado a la gestion de asistencia a las carreras!')
            opti = input('\nPresione 1 para validar un ticket\nPresione 2 para chequear la asistencia para una carrera\n>> ')
            while not opti.isnumeric() or int(opti) not in range(1,3):
                opti = input('\nERROR - Ingreso Invalido\nPresione 1 para validar un ticket y confirmar asistencia\nPresione 2 para chequear la asistencia para una carrera\n>> ')
            if opti == '1':
                print('\n----- VALIDACION DE TICKETS -----')
                try:
                    carreras, codigos = confirmar_asistencia(clientes, codigos, carreras)
                except:
                    print('Lo sentimos, su ticket no es valido')
            elif opti == '2':
                print('\n----- CHEQUEO DE ASISTENCIA -----')
                chequear_asistencia(carreras)
            
        #4: Gestion de restaurantes
        elif opt == 4:
            print('\nUsted ha ingresado a la gestion de restaurantes!')
            cliente = verify_vip(clientes)
            if cliente == False:
                continue
            else:
                opti = input('\nPresione 1 para buscar productos por su nombre\nPresione 2 para buscar productos en un rango de precio\nPresione 3 para buscar productos por tipo\n>> ')
                while not opti.isnumeric() or int(opti) not in range(1,4):
                    opti = input('\nERROR - Ingreso Invalido\nPresione 1 para buscar productos por su nombre\nPresione 2 para buscar productos en un rango de precio\nPresione 3 para buscar productos por tipo\n>> ')
                if opti == '1':
                    print('\n----- BUSQUEDA DE PRODUCTOS POR NOMBRE -----')
                    products_nombre(restaurantes,cliente)
                elif opti == '2':
                    print('\n----- BUSQUEDA DE PRODUCTOS POR RANGO DE PRECIO -----')
                    productos_precio(restaurantes,cliente)
                elif opti == '3':
                    print('\n----- BUSQUEDA DE PRODUCTOS POR TIPO -----')
                    products_type(restaurantes,cliente)
                
        #5: Gestion de venta de restaurantes 
        elif opt == 5:
            print('\nUsted ha ingresado a la gestion de venta de restaurantes!')
            cliente = verify_vip(clientes)
            if cliente == False:
                continue
            else:
                try:
                    restaurantes, compras = get_compra(compras, cliente,restaurantes)
                except:
                    print('Se ha cancelado la compra')
                    
        #6: Estadisticas
        elif opt == 6:
            print('\nUsted ha ingresado a la seccion de estadisticas!')
            opti = input('\nPresione 1 para ver el promedio de gasto de un cliente VIP\nPresione 2 para ver la tabla de asistencia a las carreras\nPresione 3 para ver la carrera con mayor asistencia\nPresione 4 para ver la carrera con mayor boletos vendidos\nPresione 5 para ver el top 3 de productos mas vendidos\nPresione 6 para ver el top 3 de clientes\nPresione 7 para ver el grafico de las estadisticas\nPresione 8 para volver al menu inicial\n>> ')
            while not opti.isnumeric() or int(opti) not in range(1,9):
                opti = input('\nERROR - Ingreso Invalido\nPresione 1 para ver el promedio de gasto de un cliente VIP\nPresione 2 para ver la tabla de asistencia a las carreras\nPresione 3 para ver la carrera con mayor asistencia\nPresione 4 para ver la carrera con mayor boletos vendidos\nPresione 5 para ver el top 3 de productos mas vendidos\nPresione 6 para ver el top 3 de clientes\nPresione 7 para ver el grafico de las estadisticas\nPresione 8 para volver al menu inicial\n>> ')
            opti = int(opti)
            if opti ==1:
                print('\n----- PROMEDIO DE GASTO DE UN CLIENTE VIP -----')
                promedio_vip(clientes,compras)
            elif opti == 2:
                print('\n----- TABLA DE ASISTENCIA A LAS CARRERAS -----')
                
            elif opti == 3:
                print('\n----- CARRERA CON MAYOR ASISTENCIA -----')
                mayor_asistencia(carreras)
            elif opti == 4:
                print('\n----- CARRERA CON MAYOR BOLETOS VENDIDOS -----')
                mayor_boletos(carreras)
            elif opti == 5:
                print('\n----- TOP 3 PRODUCTOS VENDIDOS -----')
                max_productos(productos)
            elif opti == 6:
                print('\n----- TOP 3 CLIENTES -----')
                max_clientes(clientes)
            elif opti == 7:
                print('\n----- GRAFICO DE LAS ESTADISTICAS -----')
                
            elif opti == 8:
                pass
            
        #7: Salir
        else: 
            print('\nHasta pronto! ⚙️\n\n')
            break
    
  
main()
