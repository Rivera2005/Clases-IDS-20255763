nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
nota5 = float(input())
nota6 = float(input())

listaNotas = [nota1, nota2, nota3, nota4, nota5, nota6]
maximo = max(listaNotas)
minimo = min(listaNotas)
diferencia = maximo - minimo
suma = nota1 + nota2 + nota3 + nota4 + nota5 + nota6
promedio = suma/6

print(f"Maximo: {maximo:.2f}")
print(f"Minimo: {minimo:.2f}")
print(f"Diferencia: {diferencia:.2f}")
print(f"Suma: {suma:.2f}")
print(f"Promedio: {promedio:.2f}")
