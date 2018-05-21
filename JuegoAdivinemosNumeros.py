#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
from random import randint 

#Clase Rob (Robot)
class Rob():
    numToGuess = 0
    attemptNum = 0
    
    def __init__(self):
        self.numToGuess = randint(1, 100) #Inicializa un número aleatorio entre el 1 y el 100 cada vez que se cree un Objeto "Rob"

    def attemptGuessUserNumber(self, numMin, numMax):
        self.attemptNum = randint(numMin, numMax) #Va a crear un número aleatorio dentro del rango(numMin-numMax) donde puede encontrarse el número a adivinar del Usuario
        return self.attemptNum 

    def checkUserNumber(self, userNumber, count): #Función para comparar número del Usuario con el del Robot
        s = "" 
        
        if userNumber < self.numToGuess:
            print("\nMi número es mayor...")
            return False
        elif userNumber > self.numToGuess:
            print("\nMi número es menor...")
            return False
        else:
            print("\n¡Adivinaste! :D\n")
            if count > 1: #Es por el caso de que el intento sea más de 1, para brindar una respuesta más adecuada
                s = "s"
            print("¡Lo lograste en " + str(count) + " intento" + s + "!\n")
            return True

#Proceso para adivinar el número del Robot
def guessRobotNumber():
    rob = Rob() #Se instancia un objeto "Rob" (Robot)
    correct = False
    count = 0 #Contador inicializado en 0 para contar la cantidad de intentos del Usuario en adivinar el número del Robot

    print("¡Bien!... estoy pensando un numero entre el 1 y el 100...") 
    print("¡trata de adivinar!\n")
    while(not correct): #Va a pedir un número al Usuario hasta que de con el correcto
        userNumber = validOption(1) #Llama a la función que valida el valor ingresado por el Usuario
        count += 1 #Suma 1 al contador de intentos por cada vuelta del While
        correct = rob.checkUserNumber(userNumber, count) #Llama al método del Robot que compara el número del Usuario con el suyo

#Proceso para que el Robot adivine el número del Usuario
def guessUserNumber():
    rob = Rob() #Se instancia un objeto "Rob" (Robot)
    numMin = 1 #Se inicializa el número mínimo del rango donde puede estar el número a adivinar en 1
    numMax = 100 #Se inicialia el número máximo del rango donde puede estar el número a adivinar en 100
    correct = False #Se inicializa el booleano correct en Falso hasta que el Usuario de con el número correcto y se vuelva True
    count = 0 #Contador inicializado en 0 para contar la cantidad de intentos del Robot en adivinar el número del Usuario
    s = ""

    print("Bueno, piensa en un número del 1 al 100 y yo intentaré adivinarlo...")
    print("...¿listo?...")
    print("...ok...\n")

    while(not correct):
        robNumber = rob.attemptGuessUserNumber(numMin,numMax) #Función del Robot para que devuelva un número dentro del rango(numMin-numMax) donde puede encontrarse el número a adivinar
        print("¿Tu número es: " + str(robNumber) + "?\n")
        print("1. - Mi número es mayor...")
        print("2. - Mi número es menor...")
        print("3. - ¡Adivinaste Rob! :D\n")
        option = validOption(0) #Llama a la función que valida el valor ingresado por el Usuario
        os.system("clear") #Limpia la pantalla
        count += 1 #Suma 1 al contador de intentos por cada vuelta del While

        if option == 1:
            numMin = robNumber #En caso de que el Usuario responda que el número del Robot es menor al suyo, se asigna al numMin ese número
        elif option == 2:
            numMax = robNumber #En caso de que el Usuario responda que el número del Robot es mayor al suyo, se asigna al numMax ese número
        elif option == 3:
            correct = True
            print("Oh, ¡qué emocion! :D")
            if count > 1: #Es por el caso de que el intento sea más de 1, para brindar una respuesta más adecuada
                s = "s"
            print("¡Lo adiviné en " + str(count) + " intento" + s + "!\n")
        else: #En caso de que se ingrese una opción que no está dentro de las brindadas
            print("Ingresa una opción válida, por favor")
 
#Función para validar que se ingresen enteros
def validOption(optionOrNum):

    if optionOrNum == 0: #Condicional para hacer el pedido correspondiente al Usuario según dónde se esté llamando a esta función
        option_or_number = "una opción"
    elif optionOrNum == 1:
        option_or_number = "un número"

    while(True): #Pide un valor entero hasta que el Usuario ingrese uno
        try:
            option = int(raw_input("(Ingresa " + option_or_number + "): "))
            return option
        except ValueError:
            print("No es válido, por favor introduce un número entero.")

#Función para consultar a Usuario si desea jugar nuevamente
def playAgain():
    print("¿Quieres jugar nuevamente?")
    print("1. - Sí")
    print("2. - No, volver al menú principal.\n")
    
    while(True):
        option = validOption(0) #Llama a la función que valida el valor ingresado por el Usuario
        if option == 1:
            return True
        elif option == 2:
            os.system("clear") #Limpia la pantalla
            return False
        else: #En caso de que se ingrese una opción que no está dentro de las brindadas
            print ("Ingresa una opción válida, por favor.")

#PRINCIPAL
while True:
    again = True #Inicializa el booleano again en True hasta que la función playAgain retorne un False en caso de que el Usuario no quiera volver a jugar
    print("¡Hola! Bienvenido/a al juego: \n**** AD1V1N3M0S NUM3R0S ****")
    print("\nMi nombre es Rob, ¿qué quieres hacer?\n")
    print ("1. - Quiero adivinar TU número")
    print ("2. - Quiero que adivines MI número")
    print ("3. - Quiero salir...\n")

    option = validOption(0) #Llama a la función que valida el valor ingresado por el Usuario

    if option == 1:
        while(again):
            os.system("clear") #Limpia la pantalla
            print ("Juego: - Quiero adivinar TU número\n")
            guessRobotNumber() #Proceso para adivinar el número del Robot
            again = playAgain() #Función para jugar nuevamente
    elif option == 2:
        while(again):   
            os.system("clear") #Limpia la pantalla
            print ("Juego: - Quiero que adivines MI número\n")
            guessUserNumber() #Proceso para adivinar el número del Usuario
            again = playAgain() #Función para jugar nuevamente
    elif option == 3:
        os.system("clear") #Limpia la pantalla
        print ("\n¡Adios!\n")
        sys.exit() #Cierra el programa
    else:
        os.system("clear") #Limpia la pantalla
        print ("Ingresa una opción válida, por favor.")
