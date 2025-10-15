#------Actividad 1------
precios_frutas={"Banana": 1200, "Ananá": 2500, "Melon": 3000, "Uva": 1450}
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(precios_frutas)
#------Actividad 2------
precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melon"]=2800
print(precios_frutas)
#------Actividad 3------
frutas_sin_precios=[]
fruta=str(input("Ingrese la fruta que desea: "))
fruta=fruta.title()
if fruta in precios_frutas:
    print(f"Esa fruta vale: {precios_frutas[fruta]}")
else:
    print("Esa fruta no tiene precio")
    frutas_sin_precios.append(fruta)
print(frutas_sin_precios)
#------Actividad 4------
contactos={}
for i in range(1,6):
    nombre=str(input(f"Ingrese el {i}° nombre: "))
    nombre=nombre.title()
    numero=str(input(f"Ingrese el numero de {nombre}: "))
    contactos[nombre]=numero
print(contactos)
#------Actividad 5------
conteo_palabras={}
frase=str(input("Ingrese una frase: "))
palabras_unicas=set(frase.split())
for palabra in frase.split():
    if palabra in conteo_palabras:
        conteo_palabras[palabra]+=1
    else:
        conteo_palabras[palabra]=1
print(palabras_unicas)
print(conteo_palabras)
#------Actividad 6------#
alumnos={}
for i in range(1,4):
    nombres=input(f"Ingrese el {i}° nombre: ")
    nota1=float(input(f"Ingrese la nota 1 de {nombres}: "))
    nota2=float(input(f"Ingrese la nota 2 de {nombres}: "))
    nota3=float(input(f"Ingrese la nota 3 de {nombres}: "))
    alumnos[nombres]=(nota1, nota2, nota3)
print(alumnos)
for nombres, notas in alumnos.items():
    promedio=sum(notas)/3
    print(f"El promedio de {nombres} es: {promedio}")
#------Actividad 7------
parcial_1=set()
parcial_2=set()
cantidad_aprobados_parcial_1=int(input("Ingrese la cantidad de aprobados del primer parcial: "))
cantidad_aprobados_parcial_2=int(input("Ingrese la cantidad de aprobados del segundo parcial: "))
for i in range(1,cantidad_aprobados_parcial_1+1):
    nombres_parcial_1=input(f"Ingrese el {i}° nombre que aprobó parcial 1: ")
    parcial_1.add(nombres_parcial_1)
for i in range(1,cantidad_aprobados_parcial_2+1):
    nombres_parcial_2=input(f"Ingrese el {i}° nombre que aprobó parcial 2: ")
    parcial_2.add(nombres_parcial_2)
print(parcial_1)
print(parcial_2)
print(f"Los que aprobaron ambos parciales son: {parcial_1 & parcial_2}")
print(f"Los que aprobaron almenos un parcial son: {parcial_1 ^ parcial_2}")
print(f"Lista total de los que aprobarón al menos un parcial: {parcial_1 | parcial_2}")
#------Actividad 8------
diccionario_productos={"leche": 5, "arroz": 10, "fideos":3 ,"jabon": 12}
bandera=True
while bandera:
    print('''
        (1) si desea consultar stock
        (2) si desea agregar stock
        (3) si desea agragar un producto
        (4) si desea salir 
        ''')
    opcion=input("Ingrese la opcion que desea realizar: ")
    if opcion=="1":
        consulta=input("Ingrese el producto para saber su stock: ")
        if consulta in diccionario_productos:
            print(f"Stock {consulta}: {diccionario_productos[consulta]}")
        else:
            print("El producto ingresado no se encontró")
    if opcion=="2":
        stock_producto=input("Ingrese el producto que desea agregarle stock: ")
        if stock_producto in diccionario_productos:
            stock_agregar=int(input("Ingrese la cantidad que desea agregar: "))
            print(f"Ahora el stock de {stock_producto} es: {diccionario_productos[stock_producto]+stock_agregar}")
        else:
            print("El producto que ingreso no se encuentra")
    if opcion=="3":
        nuevo_producto=input("Ingrese el producto que desea agregar: ")
        if nuevo_producto in diccionario_productos:
            print("El producto ingresado ya se encuentra")
        else:
            stock_nuevo_producto=int(input(f"Ingrese el stock de {nuevo_producto}: "))
            diccionario_productos[nuevo_producto]=stock_nuevo_producto
            print(f"Ahora el nuevo diccionario es: {diccionario_productos}")
    if opcion=="4":
        print("chau")
        bandera=False
    else:
        print("Ingrese un valor valido")
#------Actividad 9------
def consultar_evento(dia, hora):
    evento = agenda.get((dia, hora))
    if evento:
        return (f"La actividad para {dia} a las {hora} es: {evento}")
    else:
        return (f"No hay eventos agendados para {dia} a las {hora}.")
agenda={
    ("lunes", "10"): "Reunión",
    ("martes", "15"): "Clase de ingles",
    ("miercoles", "12"): "Clase de matematica",
    ("jueves", "14"): "Reunión",
    ("viernes", "11"): "Clase de lengua",
    ("sabado"): "Descanso",
    ("domingo"): "Descanso"
}
dia=input("Ingrese el dia: ")
hora=input("Ingrese la hora: ")
print(consultar_evento(dia, hora))
#------Actividad 10------
paises_capitales={"Argentina": "Buenos Aires", "Perú": "Lima", "Brasil": "Brasilia", "Uruguay": "Montevideo"}
capitales_paises={}
for clave , valor in paises_capitales.items():
    capitales_paises[valor]=clave
print(paises_capitales)
print(capitales_paises)