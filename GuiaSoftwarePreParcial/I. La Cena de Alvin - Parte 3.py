platosPrincipales = ("Hamburguesa", "Pizza", "Tacos", "Pupusas", "Hotdog")
platoscomplementos = ("Papas fritas", "Alitas de pollo", "Ensalada", "Sopa", "Lasaña")

numeroplatoprincipal = int(input())
numeroplatocomplementario = int(input())

print(f"El pedido de Alvin es: {platosPrincipales[numeroplatoprincipal-1]} con {platoscomplementos[numeroplatocomplementario-1]}")