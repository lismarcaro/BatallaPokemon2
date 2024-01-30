#Batalla pokemon

import random #para RandRage (elegir ataque oponente)

PS_Jugador = 100 #Puntos de Salud
PS_Oponente = 100
Defensa_Oponente = 100
Defensa_Jugador = 100
ataque_oponente = random.randrange (1,5)

Ataques = {"1":"latigo", "2": "placaje", "3":"Pistola de agua", "4":"ascuas", "5":"malicioso"}
#Diccionario de ataques

while PS_Jugador > 0 and PS_Oponente > 0:
    print("Escoje tu nuevo ataque")
    print("1 = latigo, 2 = placaje, 3 = Pistola de agua, 4 = ascuas y 5 = malicioso")
    ataque_jugador = input("ataque: ")
##    ataque_jugador = ataque_jugador.lower()
    if ataque_jugador == "5":
        Defensa_Oponente = Defensa_Oponente - 10
        print("Tu ataque es: ")
        print(Ataques["5"])

    if ataque_jugador == "1": #latigo
        print("Tu ataque es: ")
        print(Ataques["1"])

        if Defensa_Oponente <= 0:
            Defensa_Oponente = 1
    elif ataque_jugador == "2":
        print("Tu ataque es: ")
        print(Ataques["2"])
        PS_Oponente -= 35 * (100/Defensa_Oponente)

    elif ataque_jugador == "3": #Pistola de agua
        print("Tu ataque es: ")
        print(Ataques["3"])

    elif ataque_jugador == "4":
        print("Tu ataque es: ")
        print(Ataques["4"])
        pass


        #Turno del Oponente, se define con un Random

    
    if ataque_oponente == 1: #latigo
        print("El ataque de tu oponente es: ")
        print(Ataques["1"])
        

        Defensa_Oponente -= 10
        if Defensa_Oponente <= 0:
            Defensa_Oponente = 1

    elif ataque_oponente == 2: #placaje
        print("El ataque de tu oponente es: ")
        print(Ataques["2"])
        PS_Oponente -= 35 * (100/Defensa_Oponente)

        
    elif ataque_oponente == 3: #Pistola de agua
        print("El ataque de tu oponente es: ")
        print(Ataques["3"])

    elif ataque_oponente == 4:
        print("El ataque de tu oponente es: ")
        print(Ataques["4"])
        pass

    elif ataque_oponente == 5:
        Defensa_Oponente = Defensa_Oponente - 10
        print("El ataque de tu oponente es: ")
        print(Ataques["5"])
      
    
    else:
        print("¿¡QUE HACES!? Tus ataques son malicioso, placaje y ascuas")
        continue
        PS_Jugador -=40
   


#Si términa el ciclo, alguien ganó
if PS_Oponente <= 0 and PS_Jugador <= 0:
    print("EMPATE")
elif PS_Oponente <= 0: #el jugador es >0
    print("PERDISTE")
