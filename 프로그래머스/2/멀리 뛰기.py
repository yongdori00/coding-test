def solution(n):
    answer = 0
    
    dp = [0] * (n + 1)
    
    #한칸전, 두칸전의 값의 합을 이용하면 됨.
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
            
    answer = dp[n] % 1234567
    return answer