# Ejercicio grupo 12

bandera = True
productos=[]
while bandera:
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Mostrar todos los productos")
    print("4. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
            producto = input("Ingrese el nombre del producto: ")
            precio = input("Ingrese el precio del producto: ")
            productos.append({"producto":producto,"precio":precio})
            print("Producto agregado")
    elif opcion == 2:
        print(productos)
        if len(productos)!=0:
            producto = input("Ingrese el nombre del producto a buscar:")
            indice=0
            while indice < len(productos):
                if productos[indice]["producto"] == producto:
                    encontrado = True
                    print(producto, "Fue encontrado dentro de la lista", "Precio", productos[indice]["precio"])
                    break  # Termina el bucle si lo encuentra
                indice += 1
            else:
                 print("producto no encontrado en el inventario") 
    elif opcion == 3:
            indice=0
            while indice < len(productos):
                producto =productos[indice]["producto"]
                precio = productos[indice]["precio"]
                print("Producto número",indice,producto," Precio ",precio)
                indice += 1 
    elif opcion == 4:
        bandera = False
    else:
            print("Opción no válida")
print("Fin del programa")