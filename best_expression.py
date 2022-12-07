import re

def add(operand, operator):
    index = 0
    for i in range(len(operator)):
        if operator[index] == '+':
            operand[index] = operand[index] + operand[index+1]
            operator.pop(index)
            operand.pop(index + 1)
            index -= 1
        index += 1

    return operator, operand

def minus(operand, operator):
    index = 0
    for i in range(len(operator)):
        if operator[index] == '-':
            operand[index] = operand[index] - operand[index+1]
            operator.pop(index)
            operand.pop(index + 1)
            index -= 1
        index += 1

    return operator, operand

def mul(operand, operator):
    index = 0
    for i in range(len(operator)):
        if operator[index] == '*':
            operand[index] = operand[index] * operand[index+1]
            operator.pop(index)
            operand.pop(index + 1)
            index -= 1
        index += 1

    return operator, operand

def case1(operand, operator):
    operator, operand = add(operand, operator)
    operator, operand = minus(operand, operator)
    operator, opreand = mul(operand, operator)
    return abs(operand[0])
def case2(operand, operator):
    operator, operand = add(operand, operator)
    operator, opreand = mul(operand, operator)
    operator, operand = minus(operand, operator)
    return abs(operand[0])
def case3(operand, operator):
    operator, operand = minus(operand, operator)
    operator, operand = add(operand, operator)
    operator, opreand = mul(operand, operator)
    return abs(operand[0])
def case4(operand, operator):
    operator, operand = minus(operand, operator)
    operator, opreand = mul(operand, operator)
    operator, operand = add(operand, operator)
    return abs(operand[0])
def case5(operand, operator):
    operator, opreand = mul(operand, operator)
    operator, operand = add(operand, operator)
    operator, operand = minus(operand, operator)
    return abs(operand[0])
def case6(operand, operator):
    operator, opreand = mul(operand, operator)
    operator, operand = minus(operand, operator)
    operator, operand = add(operand, operator)
    return abs(operand[0])

def solution(expression):
    answer = 0
    operand = re.findall(r'\d+', expression)
    operator = re.findall(r'[^\d]', expression)
    operand = list(map(int, operand))

    answer = max(case1(list(operand), list(operator)), case2(list(operand), list(operator)), case3(list(operand), list(operator)), case4(list(operand), list(operator)), case2(list(operand), list(operator)), case5(list(operand), list(operator)), case6(list(operand), list(operator)))

    return answer

print(solution("100-200*300-500+20"))

