import sys

input=sys.stdin.readline

n = int(input())

arr = []

while n > 0:
    n -= 1
    string = input().strip()
    
    if 'push' in string:
        string, num2 = string.split()
        arr.append(int(num2))
    elif string == 'top':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr) - 1])
    elif string == 'size':
        print(len(arr))
    elif string == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif string == 'pop':
        if len(arr) != 0:
            print(arr.pop())
        else:
            print(-1)

