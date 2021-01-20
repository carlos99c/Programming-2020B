import os 
os.system("cls")
from math import pi
radio=float(input("ingresa el radio::: "))

print(":::MENU:::")
print(":::[1] diametro:::")
print(":::[2] perimetro:::")
print(":::[3] area:::")

#opciones que va escoger
opc=int(input("escoge la opcione que quieres realizar:::"))
    
if opc == 1:
    diametro= radio*2
    print("el diametro de la circunferencia es ", diametro)
else:
    if opc==2:
        perimetro=2*pi*radio
        print("el perimetro de la circunferencia es ",perimetro)
    else:
        if opc==3:
            area=pi*radio**2
            print("el area de la circunferencia es ", area)    
        else:
            print("solo ahi tres opciones 1 2 3")
            print("tu has tecleado". opc)