import requests
carrera_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json')
from Restaurante import Restaurante
from Bebida import Bebida
from Comida import Comida

input('go')
def crear_mapa(filas,columnas):
    mapa = []
    for y in range(filas):
        aux = []
        for x in range(columnas):
            aux.append(False)
        mapa.append(aux)
    return mapa 

def imprimir_mapa(mapa):
    print('*'*len(mapa[1]) + 'ASIENTOS DISPONIBLES'+'*'*len(mapa[1]))
    print('\n')
    nums = '    '
    for i, x in enumerate(mapa[1]):
        if i > 8 :
            nums += str(i+1)+'|'
        else:
            nums +=  str(i+1)+'|  '
    print(nums)
    for i, x in enumerate(mapa):
        if i>8:

            auxiliar= str(i+1)
        else:
            auxiliar= str(i+1)+" "
        for y in x:
            if y ==True:
                auxiliar+="| X "
            else:
                auxiliar+="|   "

        print("   "+"-"*len(mapa[1]*4))
        print(auxiliar)

mapa = crear_mapa(10,10)
imprimir_mapa(mapa)


fila = input("Seleccione la fila:  ")
columna = input("Seleccione la columna ")

mapa[int(fila)-1][int(columna)-1]=True
imprimir_mapa(mapa)
