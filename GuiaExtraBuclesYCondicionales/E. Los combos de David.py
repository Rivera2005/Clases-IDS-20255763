N = int(input())
pa, pb, pc = map(int, input().split())
contador = 0
listacombos = []

while N > contador:
    listacombos.append(input())
    contador += 1
    
for i in listacombos:
   dañoA = i.count("A") * pa
   dañoB = i.count("B") * pb
   dañoC = i.count("C") * pc
   print(dañoA + dañoB + dañoC)