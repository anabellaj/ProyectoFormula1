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
    # for constructor in constructores:
    #     constructor.mostrar()
    
    while True:
        opt = get_option()
        
        #1: Gestion de carreras y equipos
        if opt == 1:
            print('\nHa ingresado a la gestion de carrera y equipos')
            pilotos = pilotos_objetos(pilotos_edd)
            constructores = constructores_objetos(constructores_edd, pilotos)
            circuitos = circuito_obj(carreras_edd)
            carreras = carrera_objects(carreras_edd, circuitos)
            
            
            
        #2: Gestion de venta de entradas
        elif opt == 2:
            pass
        
        #3: Gestion de asistencia a las carreras
        elif opt == 2:
            pass
        
        #4: Gestion de restaurantes
        elif opt == 2:
            pass
        
        #5: Gestion de venta de restaurantes 
        elif opt == 2:
            pass
        
        #6: Estadisticas
        elif opt == 2:
            pass
        
        #7: Salir
        else: 
            print('\nHatsa pronto! ⚙️\n\n')
            break
        
main()
