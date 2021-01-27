import os 
os.system("cls")
print("programa para la lectura del 1 al 10")

numero=int(input("ingrese un numero entero::: "))
i=0
while i<=10:
    if numero == i:
        print("el caracter se encuentra en la lista",i)
    i+=1     
    if numero > 10:
        print("el numero no se encuentra en la lista  ")
        numero=int(input("ingrese un numero entero::: "))

    if numero < 0:
        print("el numero no se encuentra en la lista",)
        numero=int(input("ingrese un numero entero::: "))
    
   