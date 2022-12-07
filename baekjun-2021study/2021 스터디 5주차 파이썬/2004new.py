import sys
from math import comb

input = sys.stdin.readline

num1, num2 = map(int, input().split())

num3 = comb(num1, num2)

cnt = 0

while num3 % 10 == 0:
    cnt += 1
    num3 //= 10

print(cnt)