import os
from random import randint, uniform 

acumulado = 0
acumulado2 = 0

os.system("cls")

print(":::::::::::::::::::::::::::::::NIVEL 1:::::::::::::::::::::::::::::")
print("Por Favor, Ingrese el numero (1) para comenzar el juego: ")
op = input()
if op == '1' :
    print("Nivel Basico De 50 Puntos")
    print("::::::::::::::::::::::::") 
    while acumulado <= 50 or acumulado2 <= 50:
        print("Turno del jugador1")
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        print("Dado 1=",dado1,"Dado 2=",dado2)
        print ("Tenia", acumulado,"+",dado1,"+",dado2)
        acumulado = acumulado+dado1+dado2 
        print("Acumulado del jugador 1:", acumulado )
        print("____________________________:")
        print("Turno jugador 2")
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        print("Numero Dado 1=",dado1,"Numero Dado 2=",dado2)
        print ("Tenia", acumulado2,"+",dado1,"+",dado2)
        acumulado2 = acumulado2+dado1+dado2
        print("Acumulado del jugador2:", acumulado2 )
        print("____________________________:")
        if acumulado > acumulado2 :
            print(":::::::::::::::::::::::::::::::GANADOR JUGADOR 1:::::::::::::::::::::::::::::")          
        elif acumulado == acumulado2:
            print(":::::::::::::::::::::::::::::::EMPATE:::::::::::::::::::::::::::::")     
        else:
            print(":::::::::::::::::::::::::::::::GANADOR JUGADOR 2:::::::::::::::::::::::::::::")
else:
    print(":::::::::::::::::::::::::::::::NUMERO DIGITADO INVALIDO:::::::::::::::::::::::::::::")