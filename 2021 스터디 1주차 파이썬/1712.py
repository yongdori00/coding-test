import sys
A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

count = 0

if B >= C:
    print(-1)
    sys.exit()
count = A / (C -B) + 1
print(int(count))