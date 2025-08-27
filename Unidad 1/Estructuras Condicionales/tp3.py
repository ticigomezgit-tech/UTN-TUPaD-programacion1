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
    print("Por favor ingrese una contraseña de netre 8 y 14 caracteres")
#Actividad 6
import random
numeros_aleatorios=[random.randint(1, 100) for i in range(50)]
from statistics import mode, median, mean
if mean(numeros_aleatorios)>median(numeros_aleatorios):
    if median(numeros_aleatorios)>mode(numeros_aleatorios):
        print("sesgo positivo")
elif mean(numeros_aleatorios)<median(numeros_aleatorios):
    if median(numeros_aleatorios)<mode(numeros_aleatorios):
        print("sesgo negativo")
elif mean(numeros_aleatorios)==median(numeros_aleatorios):
    if median(numeros_aleatorios)==mode(numeros_aleatorios):
        print("sin sesgo")