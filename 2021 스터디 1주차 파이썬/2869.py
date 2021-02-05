A, B, V = input().split()

A = int(A)
B = int(B)
V = int(V)

V -= A
day = V / (A - B)
day = int(day)
if(V > day * (A -  B)):
    day += 1

print(day + 1)