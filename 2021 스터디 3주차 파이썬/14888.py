n = (int(input()))
operand_order = 0
maximum = 0
minimum = 0

number_list = (input()).split()
operand_list = (input()).split()

for i in range(n):
    number_list[i] = int(number_list[i])

for i in range(4):
    operand_list[i] = int(operand_list[i])

for i in range(n):
    if operand_list[operand_order] == 0:
        i -= 1
        operand_order += 1
        continue
    
    
