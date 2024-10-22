# Menú de opciones
inventario = []

while True:
    print("\n \t\033[32m**** Menú de Gestión de Productos ****\033[0m \n \n")
    print("1. Alta de productos nuevos")
    print("2. Consulta de datos de productos")
    print("3. Modificar la cantidad en stock de un producto")
    print("4. Dar de baja productos")
    print("5. Listado completo de los productos")
    print("6. Lista de productos con cantidad bajo mínimo")
    print("7. Salir")

    # Solicitar al usuario que seleccione una opción 

    opcion = input("\nPor favor, selecciona una opción (1-7): ")
    if opcion.isdigit():
        opcion = int(opcion)
        print("Has seleccionado:", opcion, "\n" )
    else:
        print("Por favor, ingresa un número válido.")

   

    


    if opcion == 1:
        print("\n \t \033[32m**** 1. Alta de productos nuevos ****\033[0m\n")
        
        nombre_producto = input("Ingrese un nuevo producto: ")
        cantidad_producto = int(input("Ingrese la cantidad en stock: "))
        
         # Verificar si el producto ya existe en el inventario
        producto_encontrado = False
        for producto in inventario:
            if producto[0].lower() == nombre_producto.lower():  
                producto[1] += cantidad_producto 
                print(f"Stock de '{nombre_producto}' actualizado. Nueva cantidad: {producto[1]}")
                producto_encontrado = True
                break
        
        if not producto_encontrado:
            
        
            producto = [nombre_producto, cantidad_producto]
            inventario.append(producto)
            print(f"Se añadió '{nombre_producto}' al inventario. Cantidad añadida: '{cantidad_producto}'")
        
        
        continue
    
    elif opcion == 2:
        
        #Verifica que productos hay en el inventario y su stock
        print("\n \t \033[32m**** 2. Consulta de datos de productos ****\033[0m\n")
        
        if inventario:
            for i, producto in enumerate(inventario):
                print(f"{i + 1}. Nombre: {producto[0]}, Cantidad: {producto[1]}")
        else:
            print("El inventario está vacío.")
        
        continue
    elif opcion == 3:
        print("\n \t \033[32m**** 3. Modificar la cantidad en stock de un producto ****\033[0m\n")
        continue
    elif opcion == 4:
        print("\n \t \033[32m**** 4. Dar de baja productos ****\033[0m\n")
        continue
    elif opcion == 5:
        print("\n \t \033[32m**** 5. Listado completo de los productos ****\033[0m\n")
        continue
    elif opcion == 6:
        print("\n \t \033[32m**** 6. Lista de productos con cantidad bajo mínimo ****\033[0m\n")
        continue
    elif opcion == 7:
        print("Ud ha salido del programa.")
        break
    else:
        print("\t\033[31m---- Opcion incorrecta. Seleccione una opción entre 1 y 7. ----\033[0m")
    continue