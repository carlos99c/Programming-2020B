#scriptTemperatura.py
#Se requiere de un programa que permita recibir por consola el valor de la temperatura
#en grados centígrados, debe convertir este valor a grados Kelvin, y finalmente,
#visualizar el resultado por pantalla. Considere la siguiente fórmula: °K = °C + 273.15.

T= int (input("ingresa tu temperatura en grados centigrados:"))
K = T + 273.15
print ("su temperatura en grados kelvin es", K)
