#------Actividad 1------
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()
#------Actividad 2------
def saludar_usuario(nom):
    print(f"Hola {nom}!")
nombre=str(input("Ingrese su nombre: "))
saludar_usuario(nombre)
#------Actividad 3------
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=(input("Ingrese su edad: "))
residencia=input("Ingrese su residencia: ")
informacion_personal(nombre,apellido,edad,residencia)
#------Actividad 4------
def calcular_area(radio):
    resultado=(radio*radio)*3.14
    print(f"El area del circulo es: {resultado}")
def calcular_perimetro_circulo(radio):
    resultado=2*radio*3.14
    print(f"El perimetro del circulo es: {resultado}")
rad=int(input("Ingrese el radio del circulo: "))
calcular_area(rad)
calcular_perimetro_circulo(rad)
#------Actividad 5------
def segundos_a_horas(segundos):
    resultado=segundos/3600
    print(f"La cantidad de horas son: {resultado}")
seg=int(input("Ingrese la cantidad de segundos: "))
segundos_a_horas(seg)
#------Actividad 6------
def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado=numero*i
        print(f"{numero} X {i} = {resultado}")
num=int(input("Ingrese un numero: "))
tabla_multiplicar(num)
#------Actividad 7------
def operaciones_basicas(a, b):
    suma=a+b
    resta=a-b
    multiplacion=a*b
    division=a/b
    print(f'''
La suma es: {suma}
La resta es: {resta}
La multiplicacion es: {multiplacion}
La division es: {division}
''')
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
operaciones_basicas(num1,num2)
#------Actividad 8------
def calcular_imc(peso, altura):
    return peso/(altura**2)
p=float(input("Ingrese el peso: "))
a=float(input("Ingrese la altura: "))
print(f"Tu masa corporal es: {calcular_imc(p,a)}")
#------Actividad 9------
def celsius_a_fahrenheit(celsius):
    return (celsius*9/5)+32 
cel=float(input("Ingrese los grados Celsius: "))
print(f"El equivalente de {cel}° celsius en fahrenheit es: {celsius_a_fahrenheit(cel)}°")
#------Actividad 10------
def calcular_promedio(a,b,c):
    return (a+b+c)/3
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
print(f"El promedio de {num1}, {num2} y {num3} es: {calcular_promedio(num1,num2,num3)}")