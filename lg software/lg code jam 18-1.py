from sys import stdin

stranswer = stdin.readline()
n,m = list(map(int, stdin.readline().split()))
listn = [0 for i in range(n)]
for i in range(n):
    listn[i] = list(stdin.readline().strip())

answer = 0
length = len(stranswer)

for i in range(n):
    for j in range(m):
        if listn[i][j] == stranswer[0]:
            if m - j >= length:
                for k in range(length):
                    if listn[i][j+k] != stranswer[k]:
                        answer = 0
                        break
                
                
                
                
                
                
          
          
          
          
          
                    answer = 1
            if n - i >= length:



print(answer)