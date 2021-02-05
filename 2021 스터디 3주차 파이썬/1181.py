n = (int(input("")))
str_list = []

for i in range(0, n):
    str_list.append(input(""))

str_list.sort(key = lambda x:(len(x), x))

for i in range(0, n):
    if i == 0:
        print(str_list[0])
        continue

    if str_list[i] != str_list[i-1]:
        print(str_list[i])