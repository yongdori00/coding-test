def bfs(n, k, visited, answer, num):
    cnt = 0
    nk = 1
    
    for i in range(1, len(visited)):
        if visited[i] == False:
            cnt += 1
            
    for i in range(1, cnt):
        nk *= i

    for i in range(1, len(visited)):
        if visited[i] == True:
            continue
        if k > num + nk:
            num += nk
        else:
            visited[i] = True
            answer.append(i)
            bfs(n, k, visited, answer, num)
        

def solution(n, k):
    answer = []
    visited = [False for i in range(n + 1)]
    
    bfs(n, k, visited, answer, 0)
    
    return answer