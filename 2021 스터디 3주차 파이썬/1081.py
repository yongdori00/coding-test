n = (int(input("")))
list_judge = []

for i in range(0, n):
    inner = []
    a, b = input("").split()
    a = int(a)
    inner.append(a)
    inner.append(b)
    list_judge.append(inner)

list_judge.sort(key = lambda x:x[0])

for i in range(0, n):
    print(list_judge[i][0], end = " ")
    print(list_judge[i][1])