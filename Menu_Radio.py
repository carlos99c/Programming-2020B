import os 
os.system("cls")
from math import pi
radio=float(input("ingresa el radio de la circuferencia::: "))

opc=""
while opc<"a"or opc >"c":
    print("escoge una opcion")
    print("A  calcular el diametro ")
    print("B  calcular el perimetro ")
    print("C  calcular el area ")
    opc=input("teclea la opcion que quieres realizar:: ")
    if opc=="a":
        diametro=2*radio
        print("el diametro de la circunferencia es ",diametro)
    if opc=="b":
        perimetro=2*pi*radio
        print("el perimetro de la circunferencia es ",perimetro)
    if opc=="c":
        area=pi*radio**2
        print("el area de la circunferencia es ", area)
    else:
        print("solo hay las tres opciones a, b ,c  ", opc)


