from collections import deque

def bfs(m, n, puddles, max_sum, visited):
    global answer
    curm, curn = 0, 0
    
    queue = deque()
    queue.append([0,0])
    
    while queue:
        list_ = queue.popleft()
        curm, curn = list_[0], list_[1]
        
        if curn >= n or curm >= m:
            continue
        
        if curm - 1 >= 0 and curn - 1 >= 0:
            max_sum[curn][curm] = max_sum[curn - 1][curm] + max_sum[curn][curm - 1]
        elif curm - 1 < 0 and curn - 1 >= 0:
            max_sum[curn][curm] = max_sum[curn - 1][curm]
        elif curn - 1 < 0 and curm - 1 >= 0:
            max_sum[curn][curm] = max_sum[curn][curm - 1]
        
        if curm + 1 < m and curn < n and [curm + 2, curn + 1] not in puddles and not visited[curn][curm + 1]:
            queue.append([curm + 1, curn])
            visited[curn][curm + 1] = True
        if curm < m and curn + 1 < n and [curm + 1, curn + 2] not in puddles and not visited[curn + 1][curm]:
            queue.append([curm, curn + 1])
            visited[curn + 1][curm] = True
        
    return max_sum[n - 1][m - 1]

def solution(m, n, puddles):
    max_sum = [[0 for i in range(m)] for i in range(n)]
    visited = [[False for i in range(m)] for i in range(n)]
    max_sum[0][0] = 1
    return bfs(m, n, puddles, max_sum, visited) % 1000000007