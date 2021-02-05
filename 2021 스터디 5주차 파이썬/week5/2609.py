num1, num2 = map(int, input().split())
t_num1 = num1
t_num2 = num2

if num1 < num2:
    temp = t_num1
    t_num1 = t_num2
    t_num2 = temp

while t_num1 % t_num2 != 0:
    temp = t_num1 % t_num2
    t_num1 = t_num2
    t_num2 = temp

small = t_num2
big = (num1 // small) * num2
print(small)
print(big)