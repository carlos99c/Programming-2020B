import os
os.system ("cls")

nom=[]
ape=[]
mov=[]
mail=[]
nick=[]
cont=[]
esta=[]


print("solo se permite el registro de 10 personas ")
def registro():
    i=0
    while i<=10:
        print("registro de nuevo usuario:  ")
        nombre=input("ingresa tus nombre:  ")
        apellidos=input("ingresa tu apellidos: ")
        N_movil=int(input("ingresa tu celular:  "))
        E_mail=input("ingresa tu correo: ")
        nick_name=input("crea un asuario:  ")
        contraseña=input("ingresa una nueva contraseña: ")
        estado=(True)
        
        nom.append(nombre)
        ape.append(apellidos)
        mov.append(N_movil)
        mail.append(E_mail)
        nick.append(nick_name)
        cont.append(contraseña)
        esta.append(True)
        print (nom,"\n",ape,"\n",mail,"\n",nick,"\n",cont,"\n",esta)  
        escoge=input("Quieres ingresar otro usuario si o no: ")
        if escoge== "no":
            menu()
        i=i+1   
def ingresar():
    usuario=input("ingrese su usuario")
    contraseña=input("ingrese la contraseña")
    
def menu():
    opc=0
    while opc != "3":
        print("[1]ingresar")
        print("[2] crear cuenta de usuario")
        print("[3]salir")
        opc=input("escoga la una opcion ")
    
        if opc=="1":
            ingresar()
        elif opc=="2":
            registro()
        else:
            print("que tengas buena suerte chao")    
menu()
"""lista_A=["2,4,6,8,10,8","1,3,7,9,10"]
lista_B=["1,2,3,4,5,6","1,2,3,4,5,6"]
lista_C=["5,10,15,20,25,30","1,14,21,28,35"]
print(lista_A,"\n",lista_B,"\n,",lista_C)
def lista1():
    a=(lista_A[0])
    b=(lista_A[1])
    print(a)
    print(lista_A.count([a]))
    
lista1()"""