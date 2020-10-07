
""" se requiere de un programa que solicite
al usuario por consola y determine cual de los dos 
es el mayor"""

#import os
#os.sysitem("cls")

num1=0
num2=0
num1 = int (input("dame tu primer numero "))
num2 =int(input("dame tu segundo numero "))
if num1 > 0 and num2 > 0 :
    if num1 == num2 :
        print ("los numero ingresados son iguales ")
    else :    
        if num1>num2:
            print ("el primer numero es mayor ")
        else:
            print ("el segundo numero  es mayor ")   
else :
    print("no se aceptan valores negativos")    