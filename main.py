import requests
from functions import *
carrera_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/f8e2b420a8f9f5a27463eb29e1df63605822be13/races.json')
pilotos_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json')
constructores_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json')

def main():
    carreras = carrera_url.json()
    pilotos = pilotos_url.json()
    constructores = constructores_url.json()

    while True:
        opt = get_option()
        
        #1: Gestion de carreras y equipos
        if opt == 1:
            pass
        
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
