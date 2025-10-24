S = int(input())
if S % 2 == 0:
    parPorsterior = S + 2
    imparAnterior = S - 1
else:
    parPorsterior = S + 1
    imparAnterior = S - 2
    
print(parPorsterior)
print(imparAnterior)