import sys

string = sys.stdin.readline()
stk = []

while string != '.\n':
    for i in string:
        if i == '[' or i == '(':
            stk.append(i)
        elif ((len(stk) - 1) >= 0) and (((i == ']') and (stk[len(stk) - 1] == '[')) or ((i == ')') and (stk[len(stk) - 1] == '('))):
            stk.pop()
        elif i == ']' or i == ')':
            stk.append(i)
            break

    if len(stk) == 0:
        answer = 'yes'
    else:
         answer = 'no'

    print(answer)
    
    stk = []

    string = sys.stdin.readline()