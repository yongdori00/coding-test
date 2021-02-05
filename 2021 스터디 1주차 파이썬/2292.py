layer = 1
index = 0
num = int(input())

while num > 0:
    num -= layer
    index += 1
    layer = index * 6

print(index)