"""Convertir las estructuras de datos en objetos"""
    
def carrera_objects(edd):
    carreras = []
    pass


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

            