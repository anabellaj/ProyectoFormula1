import random
from Piloto import Piloto
from Constructor import Constructor
from Bebida import Bebida
from Carrera import Carrera
from Circuito import Circuito
from Comida import Comida
from Producto import Producto
from Restaurante import Restaurante
from Ubicacion import Ubicacion
from Cliente import Cliente
from Ticket import Ticket

"""Convertir las estructuras de datos en objetos"""
def carrera_objects(edd, circuitos):
    carreras = []
    contador = 0
    for carrera in edd:
        circ = circuitos[contador]
        rest = []
        for res in carrera['restaurants']:
            rest.append(res['name'])
        x = Carrera(carrera['round'],carrera['name'],circ, carrera['date'], rest,False, '')
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
    puntaje = 0
    pilots, constructores = [] , []
    for builder in edd:
        pilots = []
        for piloto in pilotos:
            if piloto.team == builder['id']:
                pilots.append(piloto)
        x = Constructor(builder['id'],builder['name'],builder['nationality'],pilots, puntaje)
        constructores.append(x)
    return constructores
    
def pilotos_objetos(edd):
    puntaje = 0
    pilotos = []
    for pilot in edd:
        x = Piloto(pilot['id'], pilot['permanentNumber'],pilot['code'],pilot['team'],pilot['firstName'],pilot['lastName'],pilot['dateOfBirth'],pilot['nationality'],puntaje)
        pilotos.append(x)
    return pilotos
            
"""Seleccionar opcion""" 
def get_option():
    print('\n🏎️  Bienvenido al programa de Formula 1 🏎️')
    while True:
        try:
            opt = int(input('\nPresione 1 para ingresar a la gestion de carreras y equipos\nPresione 2 para ingresar a la gestion de venta de entradas\nPresione 3 para ingresar a la gestion de asistencia a las carreras\npresione 4 para ingresar a la gestion de restaurantes\nPresione 5 para ingresar a la gestion de venta de restaurantes\nPresione 6 para visualizar las estadisticas\nPresione 7 para salir\n\nIndique el numero correspondiente a su eleccion: '))
            if opt not in range (1,8):
                raise Exception
            break
        except:
            print('\nERROR - Por favor ingrese una opcion valida')
    return opt

'''Modulo 1: Gestion de carreras y equipos'''
'''Funcion para obtener el podio de una carrera'''
def get_podio(pilotos, carreras, constructores):
    puntaje = {1:25,2:18,3:15,4:12,5:10,6:8,7:6,8:4,9:2,10:1}
    print('\nCarreras sin finalizar:')
    n_invalidos = []
    for i,carrera in enumerate(carreras):
        if carrera.podio == False:
            print('\t',i+1,carrera.nombre)
        else:
            n_invalidos.append(i+1)
    choice = input('\nIngrese el numero correspondiente a la carrera a finalizar:\n>> ')
    while not choice.isnumeric() or int(choice) not in range (1,len(carreras)+1) or int(choice) in n_invalidos:
        choice = input('\nERROR - Opcion invalida\nPor favor ingrese el numero correspondiente a la carrera a finalizar:\n>> ')
    podio = random.sample(pilotos, 10)       
    contador = 1
    for piloto in podio:
        piloto.score += puntaje[contador]
        contador += 1
    for constructor in constructores:
        for pilot in constructor.pilotos:
            if pilot in podio:
                constructor.score += pilot.score
    carreras[int(choice)-1].podio = podio
    print(f"\nPodio final para la carrera {carreras[int(choice)-1].nombre}")
    for i, piloto in enumerate(podio):
        print(f"\t{i+1}. {piloto.firstName} {piloto.lastName}\tPuntaje: {puntaje[i+1]}")
    
    return pilotos, constructores, carreras
    
'''Busqueda de constructores por paises'''
def filter_paises(constructores):
    print('\nPaises disponibles:')
    paises = {'Alemania':'German','Austria':'Austrian','Francia':'French','Inglaterra':'British','Italia':'Italian','Suiza':'Swiss','Usa':'American'}                  
    for i, k in enumerate(paises.keys()):
        print('\t',i+1,k)
    pais = input('Ingrese el nombre del pais del cual desea ver sus constructores:\n>> ').title()
    while pais not in paises.keys():
        pais = input('\nERROR - Opcion Invalida\nIngrese el nombre del pais del cual desea ver sus constructores:\n>> ').title()
    print(f"\nConstructores de {pais}")
    for constructor in constructores:
        if constructor.nacionalidad == paises[pais]:
            print('\t🏁',constructor.nombre)

'''Ver pilotos de cada constructor'''
def filter_pilots(constructores):
    print('\nConstructores disponibles:')
    for i, c in enumerate(constructores):
        print('\t',i+1,c.nombre)
    choice = input('Ingrese el numero correspondiente al constructor cuyos pilotos desea visualizar:\n>> ')
    while not choice.isnumeric() or int(choice) not in range(1,len(constructores)+1):
        choice = input('\nERROR -  Ingreso invalido\nIngrese el numero correspondiente al constructor cuyos pilotos desea visualizar:\n>> ')
    print(f"\nPilotos de {constructores[int(choice)-1].nombre}")
    for p in constructores[int(choice)-1].pilotos:
        print('🚘',end=' ')
        p.mostrar()
        print('\n')
 
'''Buscar carreras por pais del circuito''' 
def filter_carreras(carreras,circuitos):
    paises = []
    print('\nPaises de los circuitos:')
    for c in circuitos:
        if c.location.pais == 'USA':
            c.location.pais = 'United States'
        if c.location.pais not in paises:
            paises.append(c.location.pais)
    for i, p in enumerate(paises):
        print('\t',i+1,p)
    choice = input('Ingrese el nombre del pais cuyas carreras desea visualizar:\n>> ').title()
    while choice not in paises and choice != 'Uk' and choice!= 'Uae':
        choice = input('\nERROR -  Ingreso invalido\nIngrese el nombre del pais cuyas carreras desea visualizar\n>> ').title()
    if choice == 'Uae' or choice == 'Uk':
        choice = choice.upper()
    print(f"\n----- CARRERAS EN {choice} -----")
    for carrera in carreras:
        if carrera.circuito.location.pais == choice:
            print('***',end='')
            carrera.mostrar()
            
'''Buscar carreras por mes'''
def filter_months(carreras):
    meses = {'enero':'01','febrero':'02','marzo':'03','abril':'04','mayo':'05','junio':'06','julio':'07','agosto':'08','septiembre':'09','octubre':'10','noviembre':'11','diciembre':'12'}
    mes = input('Ingrese el mes cuyas carreras desea observar:\n>> ').lower()
    while mes not in meses.keys():
        mes = input('\nERROR - Ingreso Invalido!\nIngrese el mes cuyas carreras desea observar:\n>> ').lower()
    contador = 0
    print(f"Carreras durante el mes de {mes}")
    for carrera in carreras:
        month = carrera.get_month()
        if month == meses[mes]:
            carrera.mostrar()
            contador += 1
    if contador == 0:
        print(f"\nNo hay carreras durante el mes de {mes}")

'''Modulo 2: Gestion de venta de entradas'''
'''Obtener los datos del cliente'''
def get_client_data(carreras):
    clientes = []
    print('\nPor favor ingrese los datos solicitados a continuacion para poder comprar su entrada!')
    nombre = input('Nombre completo: ').title()
    identificacion = input('Numero de identificacion (sin puntos!): ')
    while not identificacion.isnumeric():
        identificacion = input('\nERROR - Ingreso Invalido\nPor favor ingrese su numero de identificacion sin puntos: ')
    edad = input('Edad: ')
    while not edad.isnumeric() or int(edad) not in range(1,101):
        edad = input('\nERROR - Ingreso Invalido\nPor favor ingrese su edad reflejada en un numero entre el 0 y 100: ')
    print('\nCircuitos disponibles:')
    for i, carrera in enumerate(carreras):
        print('\t',i+1, carrera.nombre)
    circuito = input('Ingrese el numero correspondiente al circuito al cual desee asistir: ')
    while not circuito.isnumeric() or int(circuito) not in range(1,len(carreras)+1):
        circuito = input(f"\nERROR - Ingreso Invalido\nPor favor ingrese un numero entre 1 y {len(carreras)+1} correspondiente al circuito a asistir: ")
    circuito = int(circuito)-1
    entradas = {'VIP': 340,'General':150}
    tipo_entrada = input('\nTipo de entrada: \n\tPresione 1 para VIP\n\tPresione 2 para general\n>> ')
    while not tipo_entrada.isnumeric() or int(tipo_entrada) not in range(1,3):
        tipo_entrada = input('\nERROR - Ingreso Invalido\nPresione 1 para VIP o presione 2 para general: ')
    if tipo_entrada == '1':
        tipo_entrada = 'VIP'
    else: 
        tipo_entrada ='General'
    cantidad = input(f"Cuantas entradas de tipo {tipo_entrada} desea?: ")
    while not cantidad.isnumeric():
        cantidad = input(f"\nERROR - Ingreso Invalido\nCuantas entradas de tipo {tipo_entrada} desea?: ")
    cantidad = int(cantidad)
    mapa, asientos = get_asientos(cantidad)
    if mapa == None:
        return 
    subtotal = entradas[tipo_entrada] * cantidad
    descuento = 0
    if num_ondulado(subtotal):
        descuento = subtotal*0.5
    iva = subtotal*0.16
    precio = subtotal+iva-descuento
    print(f"\n-----COMPRA DE {nombre.upper()}-----\nCarrera: {carreras[circuito].nombre}\nEntradas de tipo {tipo_entrada}: {cantidad}\nAsientos: {asientos}\nSubtotal: {subtotal}\nDescuento: {descuento}\nIVA: {iva}\nMonto total: {precio}$")
    if descuento != 0:
        print('Se ha aplicado un descuento del 50%')
    if input('\nPresione cualquier tecla para confirmar orden o presione "X" para cancelar: ').title() != 'X':
        carreras[circuito].mapa = mapa
        y = Ticket(tipo_entrada, cantidad, asientos, precio)
        x = Cliente(nombre,identificacion,edad,carrera,y)
        clientes.append(x)
        print('\nSus tickets se han comprado con exito!')
        return clientes
    else:
        print('\nOrden cancelada')

def crear_mapa(filas=10,columnas=10):
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
        
def get_asientos(cantidad):
    asientos = []
    mapa = crear_mapa()
    contador =1
    imprimir_mapa(mapa)
    while cantidad >= contador:
        asiento = {}
        fila = input(f"Seleccione la fila de su entrada numero {contador}: ")
        while not fila.isnumeric() or int(fila) not in range (1,11):
            fila = input(f"\nERROR - Ingreso Invalido\nSeleccione la fila de su entrada numero {contador}: ")
        columna = input(f"Seleccione la columna de su entrada numero {contador}: ")
        while not columna.isnumeric() or int(columna) not in range (1,11):
            columna = input(f"\nERROR - Ingreso Invalido\nSeleccione la columna de su entrada numero {contador}: ")
        mapa[int(fila)-1][int(columna)-1]=True
        asiento.update({fila: columna})
        contador += 1
        asientos.append(asiento)
    imprimir_mapa(mapa)
    if input('\nPresione cualquier tecla para continuar: ').title != 'X':
        return mapa, asientos
    
def num_ondulado(number):
    count = 0
    even_index = list(str(number))[0]
    odd_index = list(str(number))[1]
    if number < 100:
        return True
    elif even_index == odd_index:
        return False
    else:
        for x in str(number):
            if (count+2)%2 == 0:
                if x != even_index:
                    ondulado = False
                count +=1
            elif (count+2) %2 !=0:
                if x != odd_index:
                    ondulado = False
                count += 1
        if ondulado == True:
            return True
        else:
            return False