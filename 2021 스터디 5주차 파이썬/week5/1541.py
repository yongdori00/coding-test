number=[]
op=[]
index = 0
index_s = 0
front = 0
behind = 0

arr=input()

for i in range(len(arr)):
    if arr[i] == '+' or arr[i] == '-':
        op.append(arr[i])
        number.append(int(arr[index_s:i]))
        index += 1
        index_s = i + 1

number.append(int(arr[index_s:]))

for i in range(len(number) - 1):
    if op[i] == '-':
        front = i + 1
    if number[i + 1] == 0:
        continue
    if op[i] == '+':
        number[front] = number[front] + number[i+1]
        number[i + 1] = 0
        if(i + 1) == len(number) - 1:
            break

print(number)

for i in range(len(number) - 1):
    if number[i + 1] == 0 or op[i] == '+':
        continue
    if op[i] == '-':
        number[0] = number[0] - number[i + 1]
        number[i + 1] = 0
        if(i + 1) == len(number) - 1:
            break

print(number)