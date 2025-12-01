import modulo_datos as m_d

# Ejercicio: Registrar estudiante
def registrar_estudiante():
    """
    Docstring para registrar_estudiante
    
    Pide al usuario que digite el carnet, nombre, apellido del estudiante, además de ciertas validaciones que se puedan agregar el diccionario con los datos a una lista
    """
    while True:

        try:
            carnet_estudiante = input("Digite su carnet: ").strip()
        except Exception:
            # Validación de valores invalidos
            print("Error de valor al momento de digitar carnet, intente nuevamente")
            continue
            
        # Excepción de entrada vacía
        if carnet_estudiante == "":
            print("El campo de carnet no puede quedar vacio. Intente nuevamente")
            continue

        # Validación de caracteres necesarios
        if len(carnet_estudiante) < 6 or len(carnet_estudiante) > 10:
            print("El carnet debe tener entre 6 y 10 caracteres")
            continue

        # Validar si el carnet ya existe
        carnet_existe = False
        for estudiante in m_d.lista_estudiantes:
            if estudiante["carnet_estudiante"] == carnet_estudiante:
                carnet_existe = True
                break
        
        if carnet_existe:
            print("El carnet ya existe. Intente nuevamente")
            continue

        break
    
    while True:

        # Manejo de excepciones
        try:
            nombre_estudiante = input("Digite el nombre: ").strip()
        except Exception:
            print("Error al digitar el nombre. Intente nuevamente")
            continue
        
        # Verificar que le campo no quede vacio
        if nombre_estudiante == "":
            print("El campo nombre no puede quedar vacio. Intente nuevamente")
            continue

        # Verificar que el nombre tenga al menos 2 caracteres
        if len(nombre_estudiante) < 2:
            print("El nombre debe tener al menos 2 caracteres")
            continue

        break

    while True:

        # Manejo de excepciones
        try:
            apellido_estudiante = input("Digite el apellido: ").strip()
        except Exception:
            print("Error al digitar el apellido. Intente nuevamente")
            continue
        
        # Verificar que le campo no quede vacio
        if apellido_estudiante == "":
            print("El campo apellido no puede quedar vacio. Intente nuevamente")
            continue

        # Verificar que el apellido tenga al menos 2 caracteres
        if len(apellido_estudiante) < 2:
            print("El apellido debe tener al menos 2 caracteres")
            continue

        break


    estudiante = {
        "carnet_estudiante": carnet_estudiante,
        "nombre_estudiante": nombre_estudiante,
        "apellido_estudiante": apellido_estudiante
    }


    