n = (int(input("")))
y = []

for i in range(0, n):
    x = []
    a, b = (input("")).split()
    a = int(a)
    b = int(b)
    x.append(a)
    x.append(b)
    y.append(x)

y.sort(key = lambda x:(x[1], x[0]))

for i in range(0, n):
    print(y[i][0], end = " ")
    print(y[i][1])
    