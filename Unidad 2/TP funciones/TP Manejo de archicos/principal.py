#------Actividad 1------
lineas=['''nombre, precio, cantidad
arroz, 200.0, 30
fideos, 100.5, 15
polenta, 60.0, 10
''']
with open("productos.txt", "w") as archivo:
    archivo.writelines(lineas)
#------Actividad 2------
with open("productos.txt", "r") as archivo:
    lineas=archivo.readlines()
    for i in lineas[1:]:
        partes=i.strip().split(",")
        nombre = partes[0].strip()
        precio = partes[1].strip()
        cantidad = partes[2].strip()
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
#------Actividad 3------
with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    print("Productos actuales:\n")
    for linea in lineas[1:]:  
        partes = linea.strip().split(",")
        if len(partes) >= 3:
            nombre = partes[0].strip()
            precio = partes[1].strip()
            cantidad = partes[2].strip()
            print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
lineas = []
print("\nAgregar nuevo producto:")
nombre = input("Nombre: ").strip()
precio = input("Precio: ").strip()
cantidad = input("Cantidad: ").strip()
with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre}, {precio}, {cantidad}\n")
print(" Producto agregado correctamente.\n")
with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    print("Archivo actualizado:\n")
    for linea in lineas[1:]:
        partes = linea.strip().split(",")
        if len(partes) >= 3:
            nombre = partes[0].strip()
            precio = partes[1].strip()
            cantidad = partes[2].strip()
            print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
#------Actividad 4------
productos = [] 
with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
for linea in lineas[1:]:
    partes = linea.strip().split(",")
    if len(partes) == 3:
        nombre = partes[0].strip()
        precio = partes[1].strip().replace("$", "")  
        cantidad = partes[2].strip()
        precio = float(precio)
        cantidad = int(cantidad)
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        productos.append(producto)
print("Lista de productos cargada:\n")
for p in productos:
    print(p)
#------Actividad 5------
productos=[]
with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
for linea in lineas[1:]:
    partes = linea.strip().split(",")
    if len(partes) == 3:
        nombre = partes[0].strip()
        precio = partes[1].strip().replace("$", "")  
        cantidad = partes[2].strip()
        precio = float(precio)
        cantidad = int(cantidad)
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        productos.append(producto)
print("Menu")
buscarnombre = input("Ingrese el producto que quiera: ")
for p in productos:
    if p["nombre"].lower() == buscarnombre.lower():
        print("Producto encontrado!!")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")  
    elif p["nombre"].lower() !=  buscarnombre.lower():
        print("Producto no encontrado :( ")
#------Actividad 6------
productos = [] 
with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
for linea in lineas[1:]:
    partes = linea.strip().split(",")
    if len(partes) == 3:
        nombre = partes[0].strip()
        precio = partes[1].strip().replace("$", "")  
        cantidad = partes[2].strip()
        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except ValueError:
            continue
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        productos.append(producto)
print("Menú de búsqueda")
buscarnombre = input("Ingrese el nombre del producto que quiere: ").strip()
encontrado = False
for p in productos:
    if p["nombre"].lower() == buscarnombre.lower():
        print(f"\nProducto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print(f"Producto '{buscarnombre}' no encontrado.")
    opcion = input("¿Desea agregar este producto? (s/n): ").lower()
    if opcion == "s":
        nuevo_precio = float(input("Ingrese precio: "))
        nueva_cantidad = int(input("Ingrese cantidad: "))
        nuevo_producto = {
            "nombre": buscarnombre,
            "precio": nuevo_precio,
            "cantidad": nueva_cantidad
        }
        productos.append(nuevo_producto)
        print(f"Producto '{buscarnombre}' agregado correctamente.")
with open("productos.txt", "w") as archivo:
    archivo.write("NOMBRE, PRECIO, CANTIDAD\n")  
    for p in productos:
        archivo.write(f"{p['nombre']}, ${p['precio']}, {p['cantidad']}\n")
print("Archivo 'productos.txt' actualizado correctamente.")