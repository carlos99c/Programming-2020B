import os 
os.system("cls")

print("suma de los 1000 primero numeros")

n=int(input("dame el primer numero::. "))
m=int(input("dame tu segundo numero::: "))

suma=0
for i in range (n,m):
    if i %2==0:
        suma+=i
        print(i)
print(suma)