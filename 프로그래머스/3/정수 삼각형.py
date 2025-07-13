def solution(triangle):
    answer = 0
    
    dp = [[0] * (i + 1) for i in range(len(triangle))]
    
    for i in range(len(triangle)):
        #최상단의 값은 그냥 써야함.
        if i == 0:
            dp[0][0] = triangle[0][0]
            continue
        #dp문제로 이전 층에서 양쪽이 아닌 경우에는
        #오른쪽과 왼쪽 중 큰 값을 받아온다.
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i - 1][j]
            elif j == i:
                dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])
                
    answer = max(dp[-1])
    
    return answer