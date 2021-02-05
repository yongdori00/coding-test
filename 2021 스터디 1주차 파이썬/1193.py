layer = 1
num = int(input())

while num > layer:
    num -= layer
    layer += 1

if layer % 2 == 0:
    mom = layer - num + 1
    son = num
else:
    son = layer - num + 1
    mom = num

result = str(son)+"/"+str(mom)

print(result)