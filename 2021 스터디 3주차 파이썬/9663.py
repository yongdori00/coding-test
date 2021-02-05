def promissing(i):
    k = 1
    promissing = 1
    while (k < i) & promissing:
        if (num_list[i] == num_list[k]) | (abs(num_list[i] - num_list[k]) == abs(i - k)):
            promissing = 0
        k += 1
    
    return promissing

def nqueens(line, n, answer):

    if promissing(line):
        if line == n[0]:
            answer[0] += 1
        else:
            for i in range(1, n[0] + 1):
                num_list[line + 1] = i
                nqueens(line + 1, n, answer)

n = []
n.append(int(input()))
answer = [0]
num_list = [0 for i in range(n[0]+1)]

nqueens(0, n, answer)

print(answer[0])