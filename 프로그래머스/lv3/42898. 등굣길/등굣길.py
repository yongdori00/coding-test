from collections import deque

#dfs로 하다가 시간 초과 나서 bfs로 변경
def bfs(m, n, puddles, max_sum, visited):
    curm, curn = 0, 0
    
    queue = deque()
    queue.append([0,0])
    
    while queue:
        list_ = queue.popleft()
        curm, curn = list_[0], list_[1]
        
        if curn >= n or curm >= m:
            continue
        
        #x == 0, y == 0과 같은 이전의 인덱스는 배열을 벗어나는 경우를 분기
        #왼쪽, 위쪽의 max 값을 합한게 현재 위치에서 이동 갯수의 최대값이다.
        #이걸 연속해서 나아간다.
        if curm - 1 >= 0 and curn - 1 >= 0:
            max_sum[curn][curm] = max_sum[curn - 1][curm] + max_sum[curn][curm - 1]
        elif curm - 1 < 0 and curn - 1 >= 0:
            max_sum[curn][curm] = max_sum[curn - 1][curm]
        elif curn - 1 < 0 and curm - 1 >= 0:
            max_sum[curn][curm] = max_sum[curn][curm - 1]
        
        #우물이 아닌 경우에 queue에 추가해준다.
        #visited가 중요하다 visited를 하지 않으면 시간 초과 펑!(오른쪽, 아래쪽으로만 가기 때문에 visited를 사용해주는 것이 옳은 것)
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