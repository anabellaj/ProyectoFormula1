import random
import bokeh
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
from Compra import Compra

"""Convertir las estructuras de datos en objetos"""
def carrera_objects(edd, circuitos):
    carreras = []
    contador = 0
    mapa = crear_mapa()
    for carrera in edd:
        circ = circuitos[contador]
        rest = []
        for res in carrera['restaurants']:
            rest.append(res['name'])
        x = Carrera(carrera['round'],carrera['name'],circ, carrera['date'], rest,False, mapa, 0,0)
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
    productos = []
    for carrera in edd:
        for restaur in carrera['restaurants']:
            items = restaur['items']
            prod = []
            for i in items:   
                # prod = []
                subtotal = i['price']
                subtotal = float(subtotal)
                subtotal = int(subtotal)
                prod_type = i['type'].split(':')
                if prod_type[0] == 'drink':
                    if prod_type[1] == 'alcoholic':
                        y = Bebida(i['name'],300, subtotal, round(subtotal*0.16,2) ,round(subtotal*1.16,2), True)
                        prod.append(y)
                        productos.append(y)
                    else:
                        y = Bebida(i['name'],300, subtotal, round(subtotal*0.16,2),round(subtotal*1.16,2), False)
                        prod.append(y)
                        productos.append(y)
                if prod_type[0] == 'food':
                    if prod_type[1] == 'fast':
                        y =Comida(i['name'],300, subtotal, round(subtotal*0.16,2),round(subtotal*1.16,2),'Comida de empaque')
                        prod.append(y)
                        productos.append(y)
                    elif prod_type[1] == 'restaurant':
                        y =Comida(i['name'],300, subtotal, round(subtotal*0.16,2),round(subtotal*1.16,2),'Comida de preparacion')
                        prod.append(y)
                        productos.append(y)
            x = Restaurante(restaur['name'],prod, carrera['name'])
            restaurantes.append(x)
    return restaurantes, productos

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
           
'''Seleccionar opcion''' 
def get_option():
    print('\n🏎️  Bienvenido al programa de Formula 1 🏎️')
    while True:
        try:
            opt = int(input('\nPresione 1 para ingresar a la gestion de carreras y equipos\nPresione 2 para ingresar a la gestion de venta de entradas\nPresione 3 para ingresar a la gestion de asistencia a las carreras\nPresione 4 para ingresar a la gestion de restaurantes\nPresione 5 para ingresar a la gestion de venta de restaurantes\nPresione 6 para visualizar las estadisticas\nPresione 7 para salir\n\nIndique el numero correspondiente a su eleccion: '))
            if opt not in range (1,8):
                raise Exception
            break
        except:
            print('\nERROR - Por favor ingrese una opcion valida')
    return opt

'''Gestion 1: Carreras y equipos'''    
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
            print('\n\t🏁',constructor.nombre, '\n\tPuntaje: ',constructor.score)

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
    if len(n_invalidos) != len(carreras):
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
        l=[]
        for i, piloto in enumerate(podio):
            pi = piloto.firstName +' '+ piloto.lastName
            sc= puntaje[i+1]
            d= [i+1 ,pi, sc]
            l.append(d)
        print(tabulate(l,headers=['Posicion','Piloto','Puntaje']))
        return pilotos, constructores, carreras
    else:
        print('\nYa se han finalizado todas las carreras!')        
        return pilotos, constructores, carreras

'''Ver campeon mundial para el momento'''
def ganadores(pilotos, constructores):
    aux_pilotos = sorted(pilotos, key=lambda x: x.score, reverse=True)
    aux_constructores = sorted(constructores, key=lambda x: x.score,reverse=True)
    if aux_pilotos[0].score == 0:
        print('\nAun no se ha finalizado ninguna carrera!')
    else:
        print(f'Campeon mundial:\n\tPiloto: {aux_pilotos[0].firstName} {aux_pilotos[0].lastName} con {aux_pilotos[0].score} puntos\n\tConstructor: {aux_constructores[0].nombre} con {aux_constructores[0].score} puntos')

'''Gestion 2: Venta de entradas'''
'''Obtener los datos del cliente y comprar entradas'''
def get_client_data(clientes,carreras, codigos):
    print('\nPor favor ingrese los datos solicitados a continuacion para poder comprar su entrada!')
    nombre = input('Nombre completo: ')
    identificacion = input('Numero de identificacion (sin puntos!): ')
    while not identificacion.isnumeric() or identificacion in codigos:
        if not identificacion.isnumeric():
            print('\nERROR - Ingreso Invalido - Por favor ingrese su identificacion sin puntos')
        if identificacion in codigos:
            print('\nERROR - Ingreso Invalido - Ya exite un existe un ticket con la cedula ingresada')
        identificacion = input('\nPor favor ingrese su numero de identificacion sin puntos: ')
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
    c = carreras[circuito]
    mapa_aux = c.mapa
    disponibles = 100-c.boletos_vendidos
    cantidad = input(f"Cuantas entradas de tipo {tipo_entrada} desea? Solo hay {disponibles} entradas disponibles: ")
    while not cantidad.isnumeric() or int(cantidad) not in range(1,disponibles+1):
        cantidad = input(f"\nERROR - Ingreso Invalido\nCuantas entradas de tipo {tipo_entrada} desea? Recuerde que solo hay {disponibles} entrads disponibles: ")
    cantidad = int(cantidad)
    asientos = get_asientos(cantidad, mapa_aux) 
    subtotal = entradas[tipo_entrada] * cantidad
    descuento, disc = 0, False
    if num_ondulado(int(identificacion)) == True:
        disc = True
        descuento = subtotal*0.5
    iva = subtotal*0.16
    precio = subtotal+iva-descuento
    print(f"\n-----COMPRA DE {nombre.upper()}-----\nCarrera: {carreras[circuito].nombre}\nEntradas de tipo {tipo_entrada}: {cantidad}\nAsientos: {asientos}\nSubtotal: {subtotal}\nDescuento: {descuento}\nIVA: {iva}\nMonto total: {precio}$")
    if disc:
        print('Se ha aplicado un descuento del 50%')
    if input('\nPresione cualquier tecla para confirmar orden o presione "X" para cancelar: ').title() != 'X':
        y = Ticket(tipo_entrada, cantidad, asientos, precio)
        x = Cliente(nombre,identificacion,edad,c.nombre,y, descuento)
        clientes.append(x)
        codigos.append(x.identificacion)
        # for asiento in asientos:
        #     for fila,columna in asiento.items():
        #         for carrera in carreras:
        #             if carrera != c:
        #                 carrera.mapa[int(fila)-1][int(columna)-1]= False
        print('\nSus tickets se han comprado con exito!')
        c.boletos_vendidos += y.cantidad
        c.mapa = mapa_aux
        return clientes, carreras, codigos
    else:
        for asiento in asientos:
            for fila,columna in asiento.items():
                c.mapa[int(fila)-1][int(columna)-1]= False
        return None

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
        
def get_asientos(cantidad,mapa_aux):
    # r = carrera
    asientos = []
    contador =1
    imprimir_mapa(mapa_aux)
    while cantidad >= contador:
        while True:
            try: 
                asiento = {}
                fila = input(f"Seleccione la fila de su entrada numero {contador}: ")
                while not fila.isnumeric() or int(fila) not in range (1,11):
                    fila = input(f"\nERROR - Ingreso Invalido\nSeleccione la fila de su entrada numero {contador}: ")
                columna = input(f"Seleccione la columna de su entrada numero {contador}: ")
                while not columna.isnumeric() or int(columna) not in range (1,11):
                    columna = input(f"\nERROR - Ingreso Invalido\nSeleccione la columna de su entrada numero {contador}: ")
                asiento.update({fila: columna})
                if asiento in asientos:
                    raise Exception
                if mapa_aux[int(fila)-1][int(columna)-1]:
                    raise Exception
                break
            except:
                print(f"\nEl asiento {fila} {columna} ya esta ocupado. Por favor elija otro asiento.")
        asientos.append(asiento)
        mapa_aux[int(fila)-1][int(columna)-1]=True
        contador += 1
    print('Sus asientos seleccionados se representan con una "X"')
    imprimir_mapa(mapa_aux)
    return asientos
    
'''Funcion para determinar si un numero es ondulado'''
def num_ondulado(number):
    ondulado = True
    count = 0
    even_index = list(str(number))[0]
    if number in range(1,10):
        return True
    else:
        odd_index = list(str(number))[1]
    if int(number) < 100:
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
        
'''Gestion 3: Asistencia a las carreras'''
def confirmar_asistencia(clientes, codigos, carreras):
    cod = input('Ingrese el numero de cedula con la cual compro su ticket: ')
    while not cod.isnumeric():
        cod = input('\nPor favor ingrese su numero de identificacion sin puntos: ')
    if cod in codigos:
        print('\nSu ticket es valido!')
        for cliente in clientes:
            if cliente.identificacion == cod:
                for carrera in carreras:
                    if carrera.nombre == cliente.carrera:
                        carrera.asistencia += cliente.ticket.cantidad
                        codigos.remove(cod)
                        return carreras, codigos
    else:
        return None
  
def chequear_asistencia(carreras):
    for i, carrera in enumerate(carreras):
        print('\t',i+1, carrera.nombre)
    circuito = input('Ingrese el numero correspondiente al circuito al cual desee chequear su asistencia: ')
    while not circuito.isnumeric() or int(circuito) not in range(1,len(carreras)+1):
        circuito = input(f"\nERROR - Ingreso Invalido\nPor favor ingrese un numero entre 1 y {len(carreras)+1} correspondiente al circuito a asistir: ")
    circuito = int(circuito)-1
    print(f"\nAl {carreras[circuito].nombre} asistiran {carreras[circuito].asistencia} personas.")
    
'''Gestion 4: Restaurantes'''
'''Verificar si un cliente es VIP'''
def verify_vip(clientes):
    vip = []
    for cliente in clientes:
        if cliente.ticket.tipo_entrada == 'VIP':
            vip.append(cliente.identificacion)
    ced = input('\nPor favor ingrese su numero de identificacion para poder acceder a los productos: ')
    while not ced.isnumeric():
        ced = input('\nERROR - Ingreso Invalido\nPor favor ingrese su numero de identificacion para poder acceder a los productos: ')
    if ced not in vip:
        print('Debe comprar una entrada vip para poder acceder a los productos!')
        return False
    elif ced in vip:
        print('Usted es un cliente vip!')
        return cliente
        
'''Buscar productos por nombre'''
def products_nombre(restaurantes, cliente):
    print(f"Productos disponibles en {cliente.carrera}")
    prod,go = [],False
    for r in (restaurantes):
        if r.carrera == cliente.carrera:
            for p in (r.productos):
                prod.append(p)
                go = True
    for i,p in enumerate(prod):
        print(i+1,p.nombre)
    if go:
        choice = input('\nIngrese el numero correspondiente al producto del cual desee ver su informacion completa: ')
        while not choice.isnumeric() or int(choice) not in range(1,len(prod)+1):
            print(f"\nERROR - Opcion Invalida\nRecuerde que en {cliente.carrera} solo hay {len(prod)+1} disponibles\nIngrese el numero correspondiente al producto elegido a continuacion: ")
        choice = int(choice) -1
        for i,p in enumerate(prod):
            if i == choice:
                p.mostrar()
    else:
        print(f"Lo sentimos, no hay productos disponibles en el {cliente.carrera}")

'''Buscar productos por tipo'''
def products_type(restaurantes,cliente):
    choice = input('\nPresione 1 para ver productos de tipo bebida\nPresione 2 para ver productos de tipo comida\n>> ')
    while not choice.isnumeric() or int(choice) not in range(1,3):
        choice = input('\nERROR - Ingreso Invalido\nPor favor ingrese 1 para bebidas o 2 para comidas: ')
    prod,go = [],False
    for r in (restaurantes):
        if r.carrera == cliente.carrera:
            for p in (r.productos):
                prod.append(p)
                go = True
    if choice == '1':
        print('\n\nBEBIDAS DISPONIBLES EN',(cliente.carrera).upper())
    elif choice == '2':
        print('\n\nCOMIDA DISPONIBLE EN',(cliente.carrera).upper())

    if go:
        for p in prod:
            if choice == '1':
                if isinstance(p, Bebida):
                    p.mostrar()
                    print('*****************************')
            elif choice == '2':
                if isinstance(p, Comida):
                    p.mostrar()
                    print('*****************************')
    else:
        print(f"\nLo sentimos, no hay productos en el {cliente.carrera}")
    
'''Buscar productos por rango de precio'''
def productos_precio(restaurantes, cliente):
    while True:
        try:
            minimo = int(input('Ingrese el minimo precio del producto que desea obtener: '))
            break
        except:
            print('\nERROR - Por favor ingrese un numero entero!')
    while True:
        try:
            maximo = int(input('Ingrese el maximo precio del producto que desea obtener: '))
            break
        except:
            print('\nERROR - Por favor ingrese un numero entero!')
    prod, go = [], False
    for r in (restaurantes):
        if r.carrera == cliente.carrera:
            for p in (r.productos):
                if int(float(p.total)) in range (minimo,maximo+1):
                    prod.append(p)
                    go=True
    if go:
        print(f"\nProductos disponibles en el rango de {minimo}$ a {maximo}$")
        for p in prod:
            p.mostrar()
    else:
        print(f"\nLo sentimos, no hay productos disponibles en el {cliente.carrera}")
       
'''Gestion 5: Venta de restaurante'''
'''Comprar productos pertenecientes a la carrera a la que asiste el cliente'''
def get_compra(compras, cliente, restaurantes):
    orden = {}
    precio = 0
    while True:
        print(f"Productos disponibles en {cliente.carrera}")
        prod,go = [],False
        for r in (restaurantes):
            if r.carrera == cliente.carrera:
                for p in (r.productos):
                    prod.append(p)
                    go = True
        for i,p in enumerate(prod):
            print(i+1,p.nombre)
        if go:
            choice = input('\nIngrese el numero correspondiente al producto que desee comprar: ')
            while not choice.isnumeric() or int(choice) not in range(1,len(prod)+1):
                choice = input(f"\nERROR - Opcion Invalida\nRecuerde que en {cliente.carrera} solo hay {len(prod)+1} disponibles\nIngrese el numero correspondiente al producto elegido a continuacion: ")
            choice = int(choice) -1
            while True:
                if not isinstance(prod[choice], Bebida):
                    break
                else:
                    if prod[choice].alcoholico and int(cliente.edad) < 18:
                        choice = input('Recuerde que los menores de edad no pueden comprar bebidas alcoholicas!\nPor favor seleccione otro producto: ')
                        while not choice.isnumeric() or int(choice) not in range(1,len(prod)+1):
                            choice = input(f"\nERROR - Opcion Invalida\nRecuerde que en {cliente.carrera} solo hay {len(prod)+1} disponibles\nIngrese el numero correspondiente al producto elegido a continuacion: ")
                        choice = int(choice) -1    
                        continue
                    else:
                        break
            cantidad = input(f"Cuantos {prod[choice].nombre} desea? Recuerde que solo hay {prod[choice].inventario} unidades disponibles: ")
            while not cantidad.isnumeric() or int(cantidad) not in range(1,(prod[choice].inventario)+1):
                cantidad = input('\nERROR - Ingreso Invalido\nCuantos productos desea? Por favor ingrese un numero entero: ')
            cantidad =  int(cantidad)
            if prod[choice].nombre not in orden.keys():
                orden.update({prod[choice].nombre:cantidad})
            else:
                orden[prod[choice].nombre] += cantidad
            precio += prod[choice].total * cantidad
            prod[choice].inventario -= cantidad
            if input('Presione "X" para comprar otro producto o cualquier tecla para finalizar su compra: ').title() != 'X':
                break
            else:
                continue
        else:
            print(f"Lo sentimos, no hay productos disponibles en el {cliente.carrera}")
    if perfectos(cliente.identificacion) ==  True:
        x = Compra(cliente.identificacion, orden, precio, precio*0.15, (precio-(precio*0.15)))
        print(f"\n\n\t----- COMPRA DE {cliente.nombre.upper()} -----")
        x.mostrar()
        if input('\nPresione cualquier tecla para confirmar o "X" para cancelar compra: ').title() !='X': 
            print('\nSe ha realizado la compra con exito!\n')    
            compras.append(x)
            return restaurantes, compras
        else:
            for p, cantidad in orden.items():
                for pro in prod:
                    if p == pro.nombre:
                        prod.inventario += cantidad
            print('Se ha cancelado la compra')
    else:
        x = Compra(cliente.identificacion, orden, precio, 0, precio)
        print(f"\n\t----- Compra de {cliente.nombre} -----")
        x.mostrar()
        if input('Presione cualquier tecla para confirmar o "X" para cancelar compra: ').title() !='X': 
            print('\nSe ha realizado la compra con exito!\n')  
            compras.append(x)
            return restaurantes, compras
        else:
            for p, cantidad in orden.items():
                for pro in prod:
                    if p == pro.nombre:
                        pro.inventario += cantidad
            print('Se ha cancelado la compra')
   
'''Determinar si un numero es perfecto'''
def perfectos(num):
    num = int(num)
    suma = 0
    for divisor in range(1, num):
        if (num % divisor) == 0:
            suma += divisor
    if suma == num:
        return True
    else:
        return False
    
'''Gestion 6: Estadisticas'''
'''Promedio de gasto de un cliente VIP'''
def promedio_vip(clientes, compras):
    total = 0
    contador = 0
    for cliente in clientes:
            if cliente.ticket.tipo_entrada == 'VIP':
                total += cliente.ticket.precio
                contador+=1
                if compras != []:
                    for compra in compras:
                        if cliente.identificacion == compra.cedula:
                            total += compra.total
    try: 
        promedio = total/contador
        print(f'Un cliente VIP gasta en promedio {round(promedio,2)}$')
    except:
        print('No hay clientes VIP registrados en el sistema')

'''Tabla de asistencia a las carreras'''     
from tabulate import tabulate
def tabla_asistencia(carreras):
    aux = sorted(carreras, key=lambda x: x.asistencia, reverse=True)
    l=[]
    for i, carrera in enumerate(aux):
        try:
            relacion = carrera.asistencia / carrera.boletos_vendidos
        except:
            relacion = 0
        d=[i+1,carrera.nombre,carrera.circuito.name,carrera.asistencia, carrera.boletos_vendidos, relacion]
        l.append(d)
    print(tabulate(l ,headers=['Posicion','Nombre','Estadio','Asistencia','Boletos','Relacion asistencia/boletos']))

'''Carrera con mayor asistencia'''
def mayor_asistencia(carreras):
    max, max_carrera = 0, ''
    for carrera in carreras:
        if carrera.asistencia > max:
            max = carrera.asistencia
            max_carrera = carrera.nombre
    if max == 0:
        print('\nNo se ha confirmado asistencia para ninguna carrera.')
    else:
        print(f'\nLa carrera con mayor asistencia es {max_carrera}, para la cual asistiran {max} personas.')
        aux = sorted(carreras, key=lambda x:x.asistencia, reverse=True)
        l = []
        ind =[]
        contador = 0
        for prod in aux:
            if contador < 5:
                ind.append(prod.nombre)
                l.append(prod.asistencia)
                contador+=1
            else:
                break
        data = pd.DataFrame(l,index=ind)
        total = data.sum(axis=1)
        plt.bar(total.index, total)
        plt.show()

'''Carrera con mayor boletos vendidos'''
def mayor_boletos(carreras):
    max, max_carrera = 0, ''
    for carrera in carreras:
        if carrera.boletos_vendidos > max:
            max = carrera.boletos_vendidos
            max_carrera = carrera.nombre
    if max == 0:
        print('\nNo se han vendidos boletos para ninguna carrera.')
    else:
        print(f'\nLa carrera con mayor boletos vendidos es {max_carrera}, para la cual se vendieron {max} boletos.')
        aux = sorted(carreras, key=lambda x:x.boletos_vendidos, reverse=True)
        l = []
        ind =[]
        contador = 0
        for prod in aux:
            if contador < 5:
                ind.append(prod.nombre)
                l.append(prod.boletos_vendidos)
                contador+=1
            else:
                break
        data = pd.DataFrame(l,index=ind)
        total = data.sum(axis=1)
        plt.bar(total.index, total)
        plt.show()

'''Top 3 productos mas vendidos'''
def max_productos(restaurantes):
    productos = []
    for restaurante in restaurantes:
        for p in restaurante.productos:
            productos.append(p)
    aux = sorted(productos, key=lambda x: x.inventario)
    if aux[0].inventario == 300:
        print('No se ha vendido ningun producto')
    elif aux[1].inventario == 300:
        print(f"1. {aux[0].nombre}")
    elif aux[2].inventario == 300:
        print(f"1. {aux[0].nombre}\n2. {aux[1].nombre}")
    else:
        print(f"1. {aux[0].nombre}\n2. {aux[1].nombre}\n3. {aux[2].nombre}")
    l = []
    ind =[]
    contador = 0
    for prod in aux:
        if contador < 5:
            ind.append(prod.nombre)
            l.append(300 - prod.inventario)
            contador+=1
        else:
            break
        
    if aux[0].inventario != 300:
        data = pd.DataFrame(l,index=ind)
        total = data.sum(axis=1)
        plt.bar(total.index, total)
        plt.show()

'''Top 3 clientes'''
import matplotlib.pyplot as plt
import pandas as pd
def max_clientes(clientes):
    aux = sorted(clientes, key=lambda x: x.ticket.cantidad,reverse=True)
    if len(aux) == 0:
        print('Aun no se han vendido boletos')
    elif len(aux) == 1:
        print(f"1. {aux[0].nombre}")
    elif len(aux) == 2:
        print(f"1. {aux[0].nombre}\n2. {aux[1].nombre}")
    else:
        print(f"1. {aux[0].nombre}\n2. {aux[1].nombre}\n3. {aux[2].nombre}")
    l = []
    ind =[]
    for client in aux:
        ind.append(client.nombre)
        l.append(client.ticket.cantidad)
    if len(aux) != 0:
        data = pd.DataFrame(l,index=ind)
        total = data.sum(axis=1)
        plt.bar(total.index, total)
        plt.show()
    