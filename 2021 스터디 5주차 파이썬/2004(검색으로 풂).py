def countNum(N, num):
    count = 0
    divnum = num
    while N >= divnum:
        count += (N // divnum)
        divnum *= num
    return count

N, M = map(int, input().split())

print(min(countNum(N, 5) - countNum(M, 5) - countNum(N - M, 5), countNum(N, 2) - countNum(M, 2) - countNum(N - M, 2)))