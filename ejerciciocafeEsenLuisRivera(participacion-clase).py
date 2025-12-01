aplicacion_iniciada = True
lista_productos = []
lista_clientes = []
pedidos_ordenados = []
while aplicacion_iniciada:
    print("----------------Menu-----------------")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Registrar nuevo cliente")
    print("4. Mostrar Clientes")
    print("5. Registrar pedidio")
    print("6. Mostrar pedidos del día")
    print("7. Mostrar categorías disponibles")
    print("8. Salir")
    opcion_usuario = int(input("Digite le número de la función que desea: "))
    # Opción salir
    if opcion_usuario == 8:
        aplicacion_iniciada = False
    # Opción 1: Mostrar productos
    if opcion_usuario == 1:
        for i in lista_productos:
            print("---------------------")
            for clave, valor in i.items():
                print(f"{clave}: {valor}")
    # Opción 2: Agregar producto
    if opcion_usuario  == 2:
        codigo = input("Digita el codigo del producto: ")
        nombre = input("Digita el nombre del nuevo producto: ")
        categoria = input("Digita la categoria del nuevo producto: ")
        precio = float(input("Digita el precio del nuevo producto: "))
        lista_productos.append({
                "codigo_producto": codigo,
                "nombre_producto": nombre,
                "categoria": categoria,
                "precio": precio
            })
    # Opción 3: Agregar cliente
    if opcion_usuario == 3:
        codigo = input("Digita el codigo del cliente: ")
        nombre = input("Digita el nombre del nuevo cliente: ")
        correo = input("Digita la correo del nuevo cliente: ")
        telefono = input("Digita el telefono del nuevo cliente: ")
        lista_clientes.append({
            "codigo_cliente": codigo,
            "nombre_cliente": nombre,
            "correo": correo,
            "telefono": telefono
        })
    # Opción 4: Mostrar clientes
    if opcion_usuario  == 4:
        for i in lista_clientes:
            print("---------------------")
            for clave, valor in i.items():
                print(f"{clave}: {valor}")
    # Opción 5: Registrar pedido
    if opcion_usuario == 5:
        print("Clientes disponibles:")
        for cliente in lista_clientes:
            print(f"- Código: {cliente['codigo_cliente']}, Nombre: {cliente['nombre_cliente']}")

        cliente_pedido = input("Digita el código del cliente para registrar pedido: ")

        # Buscar el cliente correspondiente
        cliente_conPedido = None
        for cliente in lista_clientes:
            if cliente["codigo_cliente"] == cliente_pedido:
                cliente_conPedido = cliente
                break

        if not cliente_conPedido:
            print("⚠️ Cliente no encontrado.")
        else:
            print("Productos disponibles:")
            for producto in lista_productos:
                print(f"- Código: {producto['codigo_producto']}, Nombre: {producto['nombre_producto']}")

            productosCliente = []
            bucleProductoCliente = True

            while bucleProductoCliente:
                producto_pedido = input(f"Digita el código del producto para registrar pedido con el cliente: ")

                producto_encontrar = None
                for producto in lista_productos:
                    if producto_pedido == producto["codigo_producto"]:
                        producto_encontrar = producto
                        break

                if producto_encontrar:
                    productosCliente.append(producto_encontrar)
                    print(f"✅ Producto '{producto_encontrar['nombre_producto']}' agregado.")
                else:
                    print("⚠️ Producto no encontrado.")

                if input("¿Quieres agregar otro producto? Si/No: ").lower() == "si":
                    bucleProductoCliente = True
                else:
                    bucleProductoCliente = False

            pedidos_ordenados.append({
                "cliente_pedido": cliente_conPedido,
                "productosCliente": productosCliente
            })

            print("✅ Pedido registrado con éxito.")

    # Opción 6: Mostrar pedidos del día
    if opcion_usuario == 6:
        if not pedidos_ordenados:
            print("📭 No hay pedidos registrados.")
        else:
            for pedido in pedidos_ordenados:
                cliente = pedido["cliente_pedido"]
                productos = pedido["productosCliente"]

                print(f"\nEl cliente {cliente['nombre_cliente']} (código: {cliente['codigo_cliente']}) ha pedido:")

                total = 0
                for producto in productos:
                    print(f"  - {producto['nombre_producto']} | Precio: ${producto['precio_producto']}")
                    total += producto['precio_producto']

                print(f"Total del pedido: ${total}")

        


            
    

print("¡Que tenga un buen día!")