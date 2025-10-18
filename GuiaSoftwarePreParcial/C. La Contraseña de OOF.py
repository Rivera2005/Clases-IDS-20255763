X = int(input())
A = input()
B = input()

numerodecaracteresincio = int((len(A)/X))
numerodecaracteresfinal = int((len(B)/X))

print(f"{A[:numerodecaracteresincio]}{B[-numerodecaracteresfinal:]}")