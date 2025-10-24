N = int(input())

listaNumeros = []
contador = 0
cantidadde7 = 0
cantidadde5= 0

while N > contador:
    listaNumeros.append(int(input()))
    contador+=1

for i in listaNumeros:
    if i == 7:
        cantidadde7 += 1
    elif i == 5:
        cantidadde5 += 1
        
print(cantidadde7, cantidadde5)