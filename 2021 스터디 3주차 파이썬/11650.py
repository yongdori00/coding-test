n = (int(input("")))
x = []
ycnt = 0
yfirst = 0
ylast = 0

for i in range(0, n):
    y = []
    a,b = (input("")).split()
    a = int(a)
    b = int(b)
    y.append(a)
    y.append(b)
    x.append(y)

x.sort(key = lambda y:(y[0], y[1]))
for i in range(0, n):
    print(x[i][0], end=" ")
    print(x[i][1])