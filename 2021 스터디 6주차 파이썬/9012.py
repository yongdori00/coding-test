import sys

n = int(input())

string = ''
leftcount = 0
rightcount = 0
answer = 'NO'

for i in range(n):
    string = sys.stdin.readline().strip()
    for i in range(len(string)):
        if string[i] == '(':
            leftcount += 1
        elif string[i] == ')':
            rightcount += 1
        if leftcount < rightcount:
            answer = 'NO'
            break

    if leftcount == rightcount:
        answer = 'YES'
    else:
        answer = 'NO'
    
    string = ''
    leftcount = 0
    rightcount = 0

    print(answer)