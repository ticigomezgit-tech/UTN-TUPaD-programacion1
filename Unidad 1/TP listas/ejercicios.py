#------ACTIVIDAD 1------
multiplos_de_4=[1,101]
for i in range(1,101):
    if i%4==0:
        print(i)
    else:
        pass
#------ACTIVIDAD 2------
lista=[12, 10, 21, 50, 100]
penultimo=lista[3]
print("la lista contiene:", lista)
print("el penultimo de la lista es:", penultimo)
#------ACTIVIDAD 3------
lista_vacia=[]
lista_vacia.append("Ticiano")
lista_vacia.append("Gomez")
lista_vacia.append("UTN")
print(lista_vacia)
#------ACTIVIDAD 4------
animales=["perro", "gato", "conejo", "pez"]
print("la lista original es:", animales)
animales[1]="loro"
animales[3]="oso"
print("la nueva lista es:", animales)
#------ACTIVIDAD 5------
numeros=[8, 15, 3, 22, 7]
#se crea una lista
numeros.remove(max(numeros))
#A mi parecer esto elimina el valor maximo de la lista numeros
print(numeros)
#Aca muestra la lista con el valor eliminado
#------ACTIVIDAD 6------
lista=[]
for i in range(10, 31, 5):
    lista.append(i)
print("la lista es:",lista)
print("el 1° numero de la lista es:",lista[0])
print("el 2° numero de la lista es:",lista[1])
#------ACTIVIDAD 7------
autos=["sedan", "polo", "suran", "gol"]
autos[1]="coupe"
autos[2]="ranger"
#------ACTIVIDAD 8------
doble=[]
doble.append(5*2)
doble.append(10*2)
doble.append(15*2)
print("la lista es:", doble)
#------ACTIVIDAD 9------
compras=[["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1]=("tallarines")
compras[0].remove("pan")
print(compras)
#------ACTIVIDAD 10------
lista_anidada=[15, True, [25,5, 57.9, 30.6], False]
print("La lista anidada es:", lista_anidada)