from collections import deque

def solution(x, y, n):
    answer = -1
    
    list_ = [1000001 for i in range(y + 1)]
    
    list_[x] = 0
    
    for i in range(x, y + 1):
        if list_[i] == 1000001:
            continue
        if i + n < y + 1:
            list_[i + n] = min(list_[i + n], list_[i] + 1)
        if i * 2 < y + 1:
            list_[i * 2] = min(list_[i * 2], list_[i] + 1)
        if i * 3 < y + 1:
            list_[i * 3] = min(list_[i * 3], list_[i] + 1)
    
    if list_[y] != 1000001:
        answer = list_[y]
    return answer
#     queue = deque()
#     queue.append([y, 0])
    
#     while queue:
#         now = queue.popleft()
#         if now[0] - n >= x:
#             queue.append([now[0] - n, now[1] + 1])
#             if (now[0] - n == x) and (answer > now[1] + 1):
#                 answer = now[1] + 1
#         if now[0] % 2 == 0:
#             queue.append([now[0] // 2, now[1] + 1])
#             if (now[0] // 2 == x) and (answer > now[1] + 1):
#                 answer = now[1] + 1
#         if now[0] % 3 == 0:
#             queue.append([now[0] // 3, now[1] + 1])
#             if (now[0] // 3 == x) and (answer > now[1] + 1):
#                 answer = now[1] + 1
    
#     if answer == 10000001:
#         answer = -1
            
#    return answer