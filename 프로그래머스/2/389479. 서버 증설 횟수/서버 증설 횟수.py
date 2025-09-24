def solution(players, m, k):
    answer = 0
    server_queue = []
    
    for i in players:
        servers = i // m
        
        while len(server_queue) != 0 and server_queue[0] == 0:
            server_queue.pop(0)
            
        length = len(server_queue)
        while length < servers:
            answer += 1
            server_queue.append(k)
            servers -= 1
        for j in range(len(server_queue)):
            server_queue[j] -= 1
    
    return answer