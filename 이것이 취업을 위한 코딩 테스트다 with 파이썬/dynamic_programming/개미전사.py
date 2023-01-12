n = int(input())

d = [0] * (n)

num_list = list(map(int, input().split()))

#내가 짠 코드(d[i-1]이 큰지, d[i-2] + num_list[i]가 큰지로 비교가 아니라서 결국은 틀림.)
d[0], d[1] = num_list[0], num_list[1]

for i in range(2, n):
    d[i] = max(d[:i - 1]) + num_list[i]

#이게 해답
d[0] = num_list[0]
d[1] = max(num_list[0], num_list[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + num_list[i])

print(d)
print(max(d))