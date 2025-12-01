lista_clientes = [] # Lista para almacenar los diccionarios con la información de los clientes
servicios_contratados = [] 
servicios_disponibles = [
    {
        "codigo": "WD",
        "descripcion": "Desarrollo Web"
    },
    {
        "codigo": "DS",
        "descripcion": "Ciencia de Datos"
    }, 
    {
        "codigo": "ML",
        "descripcion": "Machine Learning Aplicado"
    },
    {
        "codigo": "API",
        "descripcion": "Desarrollo de APIs Empresariales"
    }
]

def crear_cliente(lista_clientes):
    """
    Esta función crea los clientes y los almacena en un diccionario,
    los agrega luego a la lista de clientes.
    """ 

    while True:
        try:
            dui_cliente = input("Digite su número de DUI: ").strip()
        except Exception:
            print("Hubo un error al digitar tu DUI. Intenta nuevamente")
            continue

        # Validar que no este vacio
        if dui_cliente == "":
            print("El campo de DUI no puede estar vacio. Intente nuevamente")
            continue
        
            
        # Validación de longitued exacta
        if len(dui_cliente) != 10:
            print("El DUI debe tener 10 caracteres")
            continue

        # Validación si esta repetido
        dui_repetido = False
        for cliente in lista_clientes:
            # Validación de que el DUI no este repetido
            if cliente["dui_cliente"] == dui_cliente:
                dui_repetido = True
                break
        
        if dui_repetido:
            print("El DUI ya esta registrado, digita otro dui")
            continue

        break
            
    while True:
        nombre_cliente = input("Digite su nombre: ")

        # Validación de que el nombre tenga al menos 2 caracteres
        if len(nombre_cliente) < 2:
            print("El nombre debe tener al menos 2 caracteres")
            continue
        else:
            break

    while True:
        apellido_cliente = input("Digite su apellido: ")

        # Validación de que el nombre tenga al menos 2 caracteres
        if len(apellido_cliente) < 2:
            print("El apellido debe tener al menos 2 caracteres")
            continue
        else:
            break

    cliente = {
        "dui_cliente": dui_cliente,
        "nombre_cliente": nombre_cliente,
        "apellido_cliente": apellido_cliente
    }

    lista_clientes.append(cliente)
    print("Se registro de manera correcta el nuevo cliente")

def contratar_servicio(lista_clientes, servicios_disponibles, servicios_contratados):

    while True:
        dui_cliente_contrato = input("Digite el DUI del cliente a contratar: ")

        # Validación si el cliente existe
        cliente_encontrado = None
        for cliente in lista_clientes:
            if cliente["dui_cliente"] == dui_cliente_contrato:
                cliente_encontrado = cliente
                break
        
        if cliente_encontrado is None:
            print("El DUI no existe. Intente de nuevo")
            continue
        
        # Validación si ya tiene servicio contratado
        servicio_existente = False
        for contrato in servicios_contratados:
            if contrato["dui_cliente_contrato"] == dui_cliente_contrato:
                servicio_existente = True
                break
        
        if servicio_existente:
            print("El cliente ya tiene un servicio contratado. Intente otro cliente")
            continue

        break

    for disponible in servicios_disponibles:
        print(f"Código: {disponible['codigo']}")
        print(f"Descripción: {disponible['descripcion']}")
        print("-" * 6)

    while True:
        codigo_servicio_contrato = input("Ingrese el código del servicio a contratar: ")

        # Validación de si existe codigo
        codigo_contrato_existe = False
        for servicio_disponible in servicios_disponibles:
            if servicio_disponible["codigo"] == codigo_servicio_contrato:
                codigo_contrato_existe = True
                break
        
        if codigo_contrato_existe is False:
            print("El codigo digitado no existe. Intente nuevamente")
            continue

        break

    servicio = {
        "dui_cliente_contrato": dui_cliente_contrato,
        "codigo_servicio_contrato": codigo_servicio_contrato
    }

    servicios_contratados.append(servicio)
    print("Se agrego el servicio de manera correcta")

def listar_clientes_servicios(lista_clientes, servicios_contratados):
    
    if len(servicios_contratados) < 1:
        print("No hay contrataciones")
        return
    
    print("- WD")
    print("- DS")
    print("- ML")
    print("- API")
    print("- No contratados")
    opcion = input("Seleccione una opción: ")
    
    match opcion:
        case "WD":
            encontrados = 0

            for servicio in servicios_contratados:
                if servicio["codigo_servicio_contrato"] == "WD":
                    print(f"DUI del cliente con contrato WD: {servicio['dui_cliente_contrato']}")
                    encontrados += 1
            
            if encontrados == 0:
                print("No hay clientes con este servicio")

        case "DS":
            encontrados = 0

            for servicio in servicios_contratados:
                if servicio["codigo_servicio_contrato"] == "DS":
                    print(f"DUI del cliente con contrato DS: {servicio['dui_cliente_contrato']}")
                    encontrados += 1
            
            if encontrados == 0:
                print("No hay clientes con este servicio")

        case "ML":
            encontrados = 0

            for servicio in servicios_contratados:
                if servicio["codigo_servicio_contrato"] == "ML":
                    print(f"DUI del cliente con contrato ML: {servicio['dui_cliente_contrato']}")
                    encontrados += 1
            
            if encontrados == 0:
                print("No hay clientes con este servicio")

        case "API":
            encontrados = 0

            for servicio in servicios_contratados:
                if servicio["codigo_servicio_contrato"] == "API":
                    print(f"DUI del cliente con contrato API: {servicio['dui_cliente_contrato']}")
                    encontrados += 1
            
            if encontrados == 0:
                print("No hay clientes con este servicio")

        case "No contratados":
           
           for cliente in lista_clientes:
            tiene_contrato = False

            for servicio in servicios_contratados:
                if servicio["dui_cliente_contrato"] == cliente["dui_cliente"]:
                    tiene_contrato = True
                    break

            if not tiene_contrato:
                print(f"DUI: {cliente['dui_cliente']}")
                print(f"Nombre: {cliente['nombre_cliente']}")
                print(f"Apellido: {cliente['apellido_cliente']}")
                print("-" * 6)
    
def salir_programa():
    print("Saliendo del programa ...")
    return False

inicio_programa = True
while inicio_programa:
    print("-----Menú-----")
    print("1. Crear cliente")
    print("2. Contratar servicio")
    print("3. Listar clientes por servicio")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        crear_cliente(lista_clientes)
    elif opcion == 2:
        contratar_servicio(lista_clientes, servicios_disponibles, servicios_contratados)
    elif opcion == 3:
        listar_clientes_servicios(lista_clientes, servicios_contratados)
    elif opcion == 4:
        inicio_programa = salir_programa()
    else:
        print("Seleccione una opcion del menú")