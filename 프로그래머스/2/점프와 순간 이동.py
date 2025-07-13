def solution(n):
    ans = 0
    

    #dp 풀이 방법(효율성 실패)
#     dp = [0] * (n + 1)
    
#     for i in range(1, n + 1):
        # 홀수 일 떄는 이전 위치의 값을 더하기
#         if i % 2 == 1:
#             dp[i] = dp[i - 1] + 1
        # 짝수 일 떄는 이전 위치 vs // 2위치 비교
#         else:
#             dp[i] = min(dp[i // 2], dp[i - 1])

#     ans = dp[n]

    #문제 자체가 수학 문제였으므로 그냥 n을 연산하면 됨.
    while n > 0:
        # 홀수일 때만 값 증가(홀수일 떄만 직접 이동)
        if n % 2 == 1:
            n -= 1
            ans += 1
        else:
            n //= 2
    return ans