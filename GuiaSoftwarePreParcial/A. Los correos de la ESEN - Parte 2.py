"""
El correo contiene exactamente un @
Antes y después del @ debe haber al menos 3 caracteres
El correo debe contener al menos un punto
El correo no puede contener espacios
El correo no puede iniciar ni terminar con un punto
"""

correo = input()

condicion1 = correo.count("@") == 1
indexarroba = correo.index("@")
condicion2 = len(correo[indexarroba:]) >= 3 and len(correo[:indexarroba]) >= 3
condicion3 = correo.count(".") >= 1
condicion4 = correo.count(" ") == 0
condicion5 = correo[0] != "." and correo [-1] != "."

print(condicion1 and condicion2 and condicion3 and condicion4 and condicion5)