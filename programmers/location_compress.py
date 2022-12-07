import sys

input = sys.stdin.readline

number = int(input())
question = list(map(int, input().split()))

question2 = sorted(set(question))
new_q = {question2[i]:i for i in range(len(question2))}

for i in question:
    print(new_q[i], end=' ')