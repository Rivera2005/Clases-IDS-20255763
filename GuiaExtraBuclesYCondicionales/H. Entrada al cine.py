A = int(input())

contador = 0
listaedades = []
personasAptas = 0

while A > contador:
    listaedades.append(int(input()))
    contador += 1

for i in listaedades:
    if i >= 15:
        personasAptas += 1

print(personasAptas)