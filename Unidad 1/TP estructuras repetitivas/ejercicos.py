#------ACTIVIDAD 1------
for i in range(1,101):
    print(i)
#------ACTIVIDAD 2------
numero=int(input("ingrese un numero entero: "))
digitos=0
if numero==0:
    digitos=1
else:
    while numero>0:
        numero//=10
        digitos+=1
print("el numero ingresado tiene:", digitos, "digitos")
#------ACTIVIDAD 3------
numero1=int(input("ingrese el 1° numero: "))
numero2=int(input("ingrese el 2° numero: "))
suma=0
for i in range(numero1+1, numero2):
    suma+=i
print("la suma de los valores entre el", numero1,"y", numero2,"es:", suma)
#------ACTIVIDAD 4------
numero1=int(input("ingrese un numero: "))
cont=1
while cont==1:
    numero2=int(input("ingrese un numero (si desea acabar ingrese 0): "))
    numero1+=numero2
    suma=numero1
    if numero2==0:
        cont=0
    else:
        pass
print("la suma de los numero ingresados es:", suma)
#------ACTIVIDAD 5------
import random
numero_aleatorio=random.randint(0,9)
bandera=True
intentos=0
while bandera==True:
    numero=int(input("adivine el numero entre 0 y 9: "))
    if numero!=numero_aleatorio:
        intentos+=1
    else:
        intentos+=1
        print(f"Adivinó el numero en {intentos} intentos")
        bandera=False
#------ACTIVIDAD 6------
pares=0
for i in range(100, -1, -2):
    print(i)
print("estos son los numero pares desde el 100 hasta el 0")
#------ACTIVIDAD 7------
numero=int(input("ingrese un numero entero: "))
suma=0
for i in range(0,numero):
    suma+=i
print(f"la suma de todos los numeros entre 0 y {numero} es: {suma}")
#------ACTIVIDAD 8------
impares=0
pares=0
positivos=0
negativos=0
for i in range(1,101):
    numero=int(input(f"ingrese el {i}° numero: "))
    if numero%2==0:
        pares+=1
        if numero<0:
            negativos+=1
        else:
            positivos+=1
    else:
        impares+=1
        if numero<0:
            negativos+=1
        else:
            positivos+=1
print(f"la cantidad de numeros pares ingresador son: {pares}")
print(f"la cantidad de numeros impares ingresador son: {impares}")
print(f"la cantidad de numeros positivos ingresador son: {positivos}")
print(f"la cantidad de numeros negativos ingresador son: {negativos}")
#------AVTIVIDAD 9------
for i in range(1,101):
    numeros=int(input(f"ingrese el {i}° numero: "))
    suma+=numeros
media=suma/5
print("la media de los numeros ingresados es:", media)
#------ACTIVIDAD 10------
numero=int(input("ingrese un numero entero: "))
numero_invertido=0
if numero<0:
    print("por favor ingrese un numero positivo")
else:
    while numero>0:
        digito=numero%10
        numero_invertido=(numero_invertido*10) + digito
        numero=numero//10
print("el numero invertido es:", numero_invertido)