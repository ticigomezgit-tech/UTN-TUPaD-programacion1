#Actividad 1 
edad=int(input("ingrese su edad: "))
if edad>=18:
    print("es mayor de edad ")
#Actividad 2
nota=int(input("ingrese su nota: "))
if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")
#Actividad 3
numero_par=int(input("ingrese solo numeros pares: "))
if numero_par%2==0:
    print("Ha ingresado un numero par")
elif numero_par%2!=0:
    print("Porfavor ingrese un numero par")
#Actividad 4
edad=int(input("ingrese su edad: "))
if edad<12:
    print("Niño/a")
elif edad>=12 and edad<18:
    print("Adolescente")
elif edad>=18 and edad<30:
    print("Adulto/a joven")
elif edad>=30:
    print("Adulto/a")
#Actividad 5
longitud_minima=len("12345678")
longitud_maxima=len("123456789abcde")
contraseña=input("ingrese su contraseña: ")
if len(contraseña)>=longitud_minima and len(contraseña)<=longitud_maxima:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingrese una contraseña de entre 8 y 14 caracteres")
#Actividad 6
import random
numeros_aleatorios=[random.randint(1, 100) for i in range(50)]
from statistics import mode, median, mean
if mean(numeros_aleatorios)>median(numeros_aleatorios):
    if median(numeros_aleatorios)>mode(numeros_aleatorios):
        print(numeros_aleatorios)
        print("sesgo positivo")
elif mean(numeros_aleatorios)<median(numeros_aleatorios):
    if median(numeros_aleatorios)<mode(numeros_aleatorios):
        print(numeros_aleatorios)
        print("sesgo negativo")
elif mean(numeros_aleatorios)==median(numeros_aleatorios):
    if median(numeros_aleatorios)==mode(numeros_aleatorios):
        print(numeros_aleatorios)
        print("sin sesgo")
#Actividad 7
frase=input("ingrese una frase: ")
if frase[-1] in ("AEIOUaeiou"):
    print(frase,"!")
else:
    print(frase)
#Actividad 8
nombre=input("ingrese su nombre: ")
opcion=int(input("ingrese 1, si desea su nombre en mayusculas, ingrese 2 si desea su nombre en minusculas, y ingrese 3 si desea su numbre con la primer letra en mayusculas: "))
if opcion==1:
    nombre=nombre.upper()
    print(nombre)
elif opcion==2:
    nombre=nombre.lower()
    print(nombre)
elif opcion==3:
    nombre=nombre.title()
    print(nombre)
else:
    print("Por favor ingrese 1, 2 o 3")
#Actividad 9
magnitud=float(input("ingrese la magnitud del terremoto: "))
if magnitud<3:
    print("Muy leve")
elif magnitud>=3 and magnitud<4:
    print("Leve")
elif magnitud>=4 and magnitud<5:
    print("Moderado")
elif magnitud>=5 and magnitud<6:
    print("Fuerte")
elif magnitud>=6 and magnitud<7:
    print("Muy fuerte")
elif magnitud>=7:
    print("Extremo")
#Actividad 10
hemisferio=input("ingrese su hermisferio (N/S): ")
mes=int(input("ingrese el numero del mes: "))
dia=int(input("ingrese el numero del dia: "))
if hemisferio=="n" or hemisferio=="N":
    if (mes==3 and dia>=21) or (mes==4) or (mes==5) or (mes==6 and dia<=20):
        print("Es primavera")
    elif (mes==6 and dia>=21) or (mes==7) or (mes==8) or (mes==9 and dia<=20):
        print("Es verano")
    elif (mes==9 and dia>=21) or (mes==10) or (mes==11) or (mes==12 and dia<=20):
        print("Es otoño")
    elif (mes==12 and dia>=21) or (mes==1) or (mes==2) or (mes==3 and dia<=20):
        print("Es invierno")
if hemisferio=="s" or hemisferio=="S":
    if (mes==3 and dia>=21) or (mes==4) or (mes==5) or (mes==6 and dia<=20):
        print("Es otoño")
    elif (mes==6 and dia>=21) or (mes==7) or (mes==8) or (mes==9 and dia<=20):
        print("Es invierno")
    elif (mes==9 and dia>=21) or (mes==10) or (mes==11) or (mes==12 and dia<=20):
        print("Es primavera")
    elif (mes==12 and dia>=21) or (mes==1) or (mes==2) or (mes==3 and dia<=20):
        print("Es verano") 