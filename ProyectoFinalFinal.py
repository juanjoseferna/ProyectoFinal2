import random
import json
with open ("ranking.json") as file:
    rank=json.load(file)
salida2 =0 
nombre = input("Ingresa tu nombre: \n")
rank[nombre]= {"Partidas Ganadas": 0, "Partidas perdidas": 0}
while salida2 == 0:
    
    menu = int(input("¿Qué desea hacer? \n1. Para jugar \n2. Para ver el ranking de jugadores \n3. Para salir \n"))
    
    
    if menu == 1:
        tablero = []
        for i in range(8):
            a = []
            for x in range(8):
                a += [0]
            tablero.append(a)
        print (*tablero, sep="\n")

        def posInicial0 (tablero):
            p1 = int(input("Indique la fila (del 1 al 8) inicial \n") ) - 1
            p2 = int(input("Indique la columna (del 1 al 8) inicial \n") ) - 1
            P = [p1, p2]
            if p1 < 0 or p1 > 7 or p2 < 0 or p2 > 7:
                print ("Posición fuera del limite")
                return posInicial0 (tablero)
            elif tablero[P[0]][P[1]] == 0 and not(p1 < 0 or p1 > 7 or p2 < 0 or p2 > 7):
                    tablero[P[0]][P[1]] = 1
                    print (*tablero, sep="\n")
                    return P, tablero
            else:
                print ("Posición ocupada")
                return posInicial0 (tablero)

        P, tablero = posInicial0 (tablero)


        def B1 (tablero,P):
            direc = int(input("Direccion : \n1. Arriba \n2. Abajo \n3. Derecha \n4. Izquierda \n"))
            if direc == 1 and (tablero[P[0]-1][P[1]] == 0) and ((P[0] - 1) >= 0)  and ((P[0] - 1) <= 7):
                tablero[P[0]-1][P[1]] = 1
                print (*tablero, sep="\n")
                return (tablero)
            elif(direc == 2) and (tablero[P[0]+1][P[1]] == 0) and ((P[0] + 1) >= 0)  and ((P[0] + 1) <= 7):
                tablero[P[0]+1][P[1]] = 1
                print (*tablero, sep="\n")
                return tablero
            elif (direc == 3) and (tablero[P[0]][P[1]+1] == 0) and ((P[1] + 1) >= 0)  and ((P[1] + 1) <= 7):
                tablero[P[0]][P[1]+1] = 1
                print (*tablero, sep="\n")
                return tablero
            elif (direc == 4) and (tablero[P[0]][P[1]-1] == 0) and ((P[1] - 1) >= 0)  and ((P[1] - 1) <= 7):
                tablero[P[0]][P[1]-1] = 1
                print (*tablero, sep="\n")
                return tablero
            elif ((P[1] - 1) < 0) or ((P[0] - 1) < 0):
                print ("Intentalo con otra posición inicial")
                tablero[P[0]][P[1]] = 0
                return B1(posInicial0(tablero), posInicial0(tablero))
            else:
                print("Posicion incorrecta ó ocupada")
                return B1 (tablero,P)
            
        tablero = B1(tablero,P)
        P2 , tablero = posInicial0 (tablero)

        def B2 (tablero,P):
            direc = int(input("Direccion : \n1. Arriba \n2. Abajo \n3. Derecha \n4. Izquierda \n"))
            if direc == 1 and (tablero[P[0]-1][P[1]] == 0) and (tablero[P[0]-2][P[1]] == 0) and ((P[0] - 2) >= 0)  and ((P[0] - 2) <= 7):
                tablero[P[0]-1][P[1]] = 1
                tablero[P[0]-2][P[1]] = 1
                print (*tablero, sep="\n")
                return (tablero)
            elif(direc == 2) and (tablero[P[0]+1][P[1]] == 0) and (tablero[P[0]+2][P[1]] == 0) and ((P[0] + 2) >= 0)  and ((P[0] + 2) <= 7):
                tablero[P[0]+1][P[1]] = 1
                tablero[P[0]+2][P[1]] = 1
                print (*tablero, sep="\n")
                return tablero
            elif (direc == 3) and (tablero[P[0]][P[1]+1] == 0) and (tablero[P[0]][P[1]+2] == 0) and ((P[1] + 2) >= 0)  and ((P[1] + 2) <= 7):
                tablero[P[0]][P[1]+1] = 1
                tablero[P[0]][P[1]+2] = 1
                print (*tablero, sep="\n")
                return tablero
            elif (direc == 4) and (tablero[P[0]][P[1]-1] == 0) and (tablero[P[0]][P[1]-2] == 0) and ((P[1] + 1) >= 0)  and ((P[1] + 1) <= 7):
                tablero[P[0]][P[1]-1] = 1
                tablero[P[0]][P[1]-2] = 1
                print (*tablero, sep="\n")
                return tablero
            else:
                print("Posicion incorrecta ó ocupada")
                return B2 (tablero,P)
        tablero = B2 (tablero,P2)
        P3, tablero = posInicial0(tablero)


        def B3 (tablero,P):
            direc = int(input("Direccion : \n1. Arriba \n2. Abajo \n3. Derecha \n4. Izquierda \n"))
            if direc == 1 and (tablero[P[0]-1][P[1]] == 0) and (tablero[P[0]-2][P[1]] == 0) and (tablero[P[0]-3][P[1]] == 0) and ((P[0] - 3) >= 0) and ((P[0] - 3) <= 7):
                tablero[P[0]-1][P[1]] = 1
                tablero[P[0]-2][P[1]] = 1
                tablero[P[0]-3][P[1]] = 1
                print (*tablero, sep="\n")
                return (tablero)
            elif(direc == 2) and (tablero[P[0]+1][P[1]] == 0) and (tablero[P[0]+2][P[1]] == 0) and (tablero[P[0]+3][P[1]] == 0) and ((P[0] + 3) >= 0) and ((P[0] + 3) <= 7):
                tablero[P[0]+1][P[1]] = 1
                tablero[P[0]+2][P[1]] = 1
                tablero[P[0]+3][P[1]] = 1
                print (*tablero, sep="\n")
                return tablero
            elif (direc == 3) and (tablero[P[0]][P[1]+1] == 0) and (tablero[P[0]][P[1]+2] == 0) and (tablero[P[0]][P[1]+3] == 0) and ((P[1] + 3) >= 0) and ((P[1] + 3) <= 7):
                tablero[P[0]][P[1]+1] = 1
                tablero[P[0]][P[1]+2] = 1
                tablero[P[0]][P[1]+3] = 1
                print (*tablero, sep="\n")
                return tablero
            elif (direc == 4) and (tablero[P[0]][P[1]-1] == 0) and (tablero[P[0]][P[1]-2] == 0) and (tablero[P[0]][P[1]-3] == 0) and ((P[1] - 3) >= 0) and ((P[1] - 3) <= 7):
                tablero[P[0]][P[1]-1] = 1
                tablero[P[0]][P[1]-2] = 1
                tablero[P[0]][P[1]-3] = 1
                print (*tablero, sep="\n")
                return tablero
            else:
                print("Posicion incorrecta ó ocupada")
                return B3 (tablero,P)
            
        tablero = B3 (tablero,P3)
        P4, tablero = posInicial0(tablero)

        def B4 (tablero,P):
            direc = int(input("Direccion : \n1. Arriba \n2. Abajo \n3. Derecha \n4. Izquierda \n"))
            if direc == 1 and (tablero[P[0]-1][P[1]] == 0) and (tablero[P[0]-2][P[1]] == 0) and (tablero[P[0]-3][P[1]] == 0) and (tablero[P[0]-4][P[1]] == 0) and ((P[0] - 4)>= 0) and ((P[0] - 4)<= 7):
                tablero[P[0]-1][P[1]] = 1
                tablero[P[0]-2][P[1]] = 1
                tablero[P[0]-3][P[1]] = 1
                tablero[P[0]-4][P[1]] = 1
                print (*tablero, sep="\n")
                return (tablero)
            elif(direc == 2) and (tablero[P[0]+1][P[1]] == 0) and (tablero[P[0]+2][P[1]] == 0) and (tablero[P[0]+3][P[1]] == 0) and (tablero[P[0]+4][P[1]] == 0) and ((P[0]+ 4) <= 7) and ((P[0]+ 4) >= 0):
                tablero[P[0]+1][P[1]] = 1
                tablero[P[0]+2][P[1]] = 1
                tablero[P[0]+3][P[1]] = 1
                tablero[P[0]+4][P[1]] = 1
                print (*tablero, sep="\n")
                return tablero
            elif (direc == 3) and (tablero[P[0]][P[1]+1] == 0) and (tablero[P[0]][P[1]+2] == 0) and (tablero[P[0]][P[1]+3] == 0) and (tablero[P[0]][P[1]+4] == 0) and ((P[1] - 4) >= 0) and ((P[1] - 4) <= 7):
                tablero[P[0]][P[1]+1] = 1
                tablero[P[0]][P[1]+2] = 1
                tablero[P[0]][P[1]+3] = 1
                tablero[P[0]][P[1]+4] = 1
                print (*tablero, sep="\n")
                return tablero
            elif (direc == 4) and (tablero[P[0]][P[1]-1] == 0) and (tablero[P[0]][P[1]-2] == 0) and (tablero[P[0]][P[1]-3] == 0) and (tablero[P[0]][P[1]-4] == 0) and ((P[1] - 4) >= 0) and ((P[1] - 4) <= 7):
                tablero[P[0]][P[1]-1] = 1
                tablero[P[0]][P[1]-2] = 1
                tablero[P[0]][P[1]-3] = 1
                tablero[P[0]][P[1]-4] = 1
                print (*tablero, sep="\n")
                return tablero
            else:
                print("Posicion incorrecta ó ocupada")
                return B4 (tablero,P)

        tablero = B4 (tablero,P4)
        tableroEnemigo = []
        for i in range(8):
            a = []
            for x in range(8):
                a += [0]
            tableroEnemigo.append(a)

        def posInicialEnemiga0 (tableroEnemigo):
            p1 = random.randint(0,7)
            p2 = random.randint(0,7)
            P = [p1, p2]
            if p1 < 0 or p1 > 7 or p2 < 0 or p2 > 7:
                return posInicial0 (tableroEnemigo)
            elif tableroEnemigo[P[0]][P[1]] == 0:
                    tableroEnemigo[P[0]][P[1]] = 1
                    return P, tableroEnemigo
            else:
                return posInicialEnemiga0 (tableroEnemigo)

        PEnemigo1, tableroEnemigo = posInicialEnemiga0 (tableroEnemigo)


        def B1Enemigo (tableroEnemigo,P):
            direc = random.randint(1,4)    
            try:
                if direc == 1 and (tableroEnemigo[P[0]-1][P[1]] == 0) and (P[0]-1) >= 0:
                    tableroEnemigo[P[0]-1][P[1]] = 1
                    return (tableroEnemigo)
                elif(direc == 2) and (tableroEnemigo[P[0]+1][P[1]] == 0) and (P[0]+1) <= 7:
                    tableroEnemigo[P[0]+1][P[1]] = 1
                    return tableroEnemigo
                elif (direc == 3) and (tableroEnemigo[P[0]][P[1]+1] == 0) and (P[1]+1) <= 7:
                    tableroEnemigo[P[0]][P[1]+1] = 1
                    return tableroEnemigo
                elif (direc == 4) and (tableroEnemigo[P[0]][P[1]-1] == 0) and (P[1]-1) >= 0:
                    tableroEnemigo[P[0]][P[1]-1] = 1
                    return tableroEnemigo
                else:
                    return B1Enemigo (tableroEnemigo,P)
            except:
                return B1Enemigo(tableroEnemigo, P)

        tableroEnemigo = B1Enemigo(tableroEnemigo,PEnemigo1)
        PEnemigo2, tableroEnemigo = posInicialEnemiga0 (tableroEnemigo)

        def B2Enemigo (tableroEnemigo,P):
            direc = random.randint(1,4)
            try:
                if direc == 1 and (tableroEnemigo[P[0]-1][P[1]] == 0) and (tableroEnemigo[P[0]-2][P[1]] == 0) and (P[0]-2) >= 0:
                    tableroEnemigo[P[0]-1][P[1]] = 1
                    tableroEnemigo[P[0]-2][P[1]] = 1
                    return (tableroEnemigo)
                elif(direc == 2) and (tableroEnemigo[P[0]+1][P[1]] == 0) and (tableroEnemigo[P[0]+2][P[1]] == 0) and (P[0]+2) <= 7:
                    tableroEnemigo[P[0]+1][P[1]] = 1
                    tableroEnemigo[P[0]+2][P[1]] = 1
                    return tableroEnemigo
                elif (direc == 3) and (tableroEnemigo[P[0]][P[1]+1] == 0) and (tableroEnemigo[P[0]][P[1]+2] == 0) and (P[1]+2) <= 7:
                    tableroEnemigo[P[0]][P[1]+1] = 1
                    tableroEnemigo[P[0]][P[1]+2] = 1
                    return tableroEnemigo
                elif (direc == 4) and (tableroEnemigo[P[0]][P[1]-1] == 0) and (tableroEnemigo[P[0]][P[1]-2] == 0) and (P[1]-2) >= 0:
                    tableroEnemigo[P[0]][P[1]-1] = 1
                    tableroEnemigo[P[0]][P[1]-2] = 1
                    return tableroEnemigo
                else:
                    return B2Enemigo (tableroEnemigo,P)
            except:
                return B2Enemigo(tableroEnemigo, P)


        tableroEnemigo = B2Enemigo(tableroEnemigo, PEnemigo2) 
        PEnemigo3, tableroEnemigo = posInicialEnemiga0 (tableroEnemigo)

        def B3Enemigo (tableroEnemigo,P):
            direc = random.randint(1,4)    
            try:
                if direc == 1 and (tableroEnemigo[P[0]-1][P[1]] == 0) and (tableroEnemigo[P[0]-2][P[1]] == 0) and (tableroEnemigo[P[0]-3][P[1]] == 0) and (P[0]-3) >= 0:
                    tableroEnemigo[P[0]-1][P[1]] = 1
                    tableroEnemigo[P[0]-2][P[1]] = 1
                    tableroEnemigo[P[0]-3][P[1]] = 1
                    return (tableroEnemigo)
                elif(direc == 2) and (tableroEnemigo[P[0]+1][P[1]] == 0) and (tableroEnemigo[P[0]+2][P[1]] == 0) and (tableroEnemigo[P[0]+3][P[1]] == 0) and  (P[0]+3) <= 7:
                    tableroEnemigo[P[0]+1][P[1]] = 1
                    tableroEnemigo[P[0]+2][P[1]] = 1
                    tableroEnemigo[P[0]+3][P[1]] = 1
                    return tableroEnemigo
                elif (direc == 3) and (tableroEnemigo[P[0]][P[1]+1] == 0) and (tableroEnemigo[P[0]][P[1]+2] == 0) and (tableroEnemigo[P[0]][P[1]+3] == 0) and (P[1]+3) <= 7:
                    tableroEnemigo[P[0]][P[1]+1] = 1
                    tableroEnemigo[P[0]][P[1]+2] = 1
                    tableroEnemigo[P[0]][P[1]+3] = 1
                    return tableroEnemigo
                elif (direc == 4) and (tableroEnemigo[P[0]][P[1]-1] == 0) and (tableroEnemigo[P[0]][P[1]-2] == 0) and (tableroEnemigo[P[0]][P[1]-3] == 0) and (P[1]-3) >= 0:
                    tableroEnemigo[P[0]][P[1]-1] = 1
                    tableroEnemigo[P[0]][P[1]-2] = 1
                    tableroEnemigo[P[0]][P[1]-3] = 1
                    return tableroEnemigo
                else:
                    return B3Enemigo (tableroEnemigo,P)
            except:
                return B3Enemigo(tableroEnemigo, P)


        tableroEnemigo = B3Enemigo(tableroEnemigo, PEnemigo3) 
        PEnemigo4, tableroEnemigo = posInicialEnemiga0 (tableroEnemigo)

        def B4Enemigo (tableroEnemigo,P):
            direc = random.randint(1,4)
            try:
                if direc == 1 and (tableroEnemigo[P[0]-1][P[1]] == 0) and (tableroEnemigo[P[0]-2][P[1]] == 0) and (tableroEnemigo[P[0]-3][P[1]] == 0) and (tableroEnemigo[P[0]-4][P[1]] == 0) and (P[0]-4) >= 0:
                    tableroEnemigo[P[0]-1][P[1]] = 1
                    tableroEnemigo[P[0]-2][P[1]] = 1
                    tableroEnemigo[P[0]-3][P[1]] = 1
                    tableroEnemigo[P[0]-4][P[1]] = 1
                    return (tableroEnemigo)
                elif(direc == 2) and (tableroEnemigo[P[0]+1][P[1]] == 0) and (tableroEnemigo[P[0]+2][P[1]] == 0) and (tableroEnemigo[P[0]+3][P[1]] == 0) and (tableroEnemigo[P[0]+4][P[1]] == 0) and (P[0]+4) <= 7:
                    tableroEnemigo[P[0]+1][P[1]] = 1
                    tableroEnemigo[P[0]+2][P[1]] = 1
                    tableroEnemigo[P[0]+3][P[1]] = 1
                    tableroEnemigo[P[0]+4][P[1]] = 1
                    return tableroEnemigo
                elif (direc == 3) and (tableroEnemigo[P[0]][P[1]+1] == 0) and (tableroEnemigo[P[0]][P[1]+2] == 0) and (tableroEnemigo[P[0]][P[1]+3] == 0) and (tableroEnemigo[P[0]][P[1]+4] == 0) and (P[1]+4) <= 7:
                    tableroEnemigo[P[0]][P[1]+1] = 1
                    tableroEnemigo[P[0]][P[1]+2] = 1
                    tableroEnemigo[P[0]][P[1]+3] = 1
                    tableroEnemigo[P[0]][P[1]+4] = 1
                    return tableroEnemigo
                elif (direc == 4) and (tableroEnemigo[P[0]][P[1]-1] == 0) and (tableroEnemigo[P[0]][P[1]-2] == 0) and (tableroEnemigo[P[0]][P[1]-3] == 0) and (tableroEnemigo[P[0]][P[1]-4] == 0) and (P[1]-4) >= 0:
                    tableroEnemigo[P[0]][P[1]-1] = 1
                    tableroEnemigo[P[0]][P[1]-2] = 1
                    tableroEnemigo[P[0]][P[1]-3] = 1
                    tableroEnemigo[P[0]][P[1]-4] = 1
                    return tableroEnemigo
                else:
                    return B4Enemigo (tableroEnemigo,P)
            except:
                return B4Enemigo(tableroEnemigo, P)
                    
        tableroEnemigo = B4Enemigo(tableroEnemigo, PEnemigo4)
        numeroBarcos = 0
        numeroBarcosEnemigos = 0

        tableroDisparos = []
        for i in range(8):
            a = []
            for x in range(8):
                a += [0]
            tableroDisparos.append(a)

        def contarBarcos(tabla, contador):
            contador = 0
            for i in range (len(tabla)):
                for j in range(len(tabla[i])):
                    if tabla[i][j] == 1:
                        contador += 1
            return contador 

        def disparo1 ():
            print("------------------------")
            fila = (int(input("Ingrese la fila (del 1 al 8) del disparo")) - 1)
            hilera = (int(input("Ingrese la hilera (del 1 al 8) del disparo")) - 1)
            if fila >= 0 and fila <= 7 and hilera >= 0 and hilera < 8:
                return [fila, hilera]
            else:
                return disparo1()

        def caerDisparo (tablero,tablero2, disparo):
            print("------------------------")
            if tablero2[disparo[0]][disparo[1]] == 8:
                print (*tablero, sep="\n")
                print("Ya has disparado a esta posición, Intentalo de nuevo")
                return (caerDisparo(tablero,tablero2,disparo1()))
            elif tablero2[disparo[0]][disparo[1]] == 1:
                tablero[disparo[0]][disparo[1]] = 8
                tablero2[disparo[0]][disparo[1]] = 8
                print (*tablero, sep="\n")
                print ("Le has dado a un barco, sigue así ")
                return tablero,tablero2
            elif tablero2[disparo[0]][disparo[1]] == 0:
                tablero[disparo[0]][disparo[1]] = 8
                tablero2[disparo[0]][disparo[1]] = 8
                print (*tablero, sep="\n")
                print ("Intentalo en el siguiente turno")
                return tablero,tablero2


        def DisparoEnemigo (tablero):
            f = random.randint(0,7)
            h = random.randint(0,7)
            disparo = [f,h]
            if tablero[disparo[0]][disparo[1]] == 8:
                return DisparoEnemigo(tablero)
            elif tablero[disparo[0]][disparo[1]] == 1:
                tablero[disparo[0]][disparo[1]] = 8
                print ("Te han dado")
                return tablero
            elif tablero[disparo[0]][disparo[1]] == 0:
                tablero[disparo[0]][disparo[1]] = 8
                print ("El enemigo ha fallado")
                return tablero

        salida = 0

        while salida == 0:


            disparo = []
            disparo = disparo1()
            tableroDisparos,tableroEnemigo = caerDisparo(tableroDisparos,tableroEnemigo,disparo)
            print("Te quedan", numeroBarcosEnemigos, "por hundir")
            tablero = DisparoEnemigo (tablero)
            numeroBarcos = contarBarcos(tablero, numeroBarcos)
            numeroBarcosEnemigos = contarBarcos (tableroEnemigo, numeroBarcosEnemigos)
            if numeroBarcos == 0:
                print ("Te has quedado sin barcos")
                print("Intentalo en otra partida")
                rank [nombre]["Partidas perdidas"] += 1
                salida = 1
            if numeroBarcosEnemigos == 0:
                print("Has derrotado todos los barcos")
                print ("Felicitaciones!, Ha ganado el juego")
                rank[nombre]["Partidas Ganadas"] += 1
                salida = 1

    elif menu == 2:
        print(rank)
        
    elif menu == 3:
        print("Hasta la proxima")
        salida2 = 1
    with open ("ranking.json","a") as archivo: 
        json.dump(rank,archivo)
