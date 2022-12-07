from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7,8],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

queue = deque()

visited = [False] * 9

def bfs(graph, v, visited):
    global queue

    # queue는 stack이랑 달리 while문 안에서 동작한다.
    while queue:
        for i in graph[v]:
            if visited[i] is False:
                visited[i] = True
                queue.append(i)

        v = queue.popleft()

        print(v, end=' ')
    

queue.append(1)
visited[1] = True
bfs(graph, 1, visited)