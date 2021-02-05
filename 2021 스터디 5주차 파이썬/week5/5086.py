num1, num2 = map(int, input().split())

answer = ''

while num1 != 0 and num2 != 0:
    if num1 > num2 and num1 % num2 == 0:
        answer = 'multiple'
    elif num1 < num2 and num2 % num1 == 0:
        answer = 'factor'
    else:
        answer = 'neither'

    print(answer)
    
    num1, num2 = map(int, input().split())