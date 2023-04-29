#결국 x~y 과정을 모두 min으로 연산하는 문제임.
def solution(x, y, n):
    answer = -1
    
    #0~y까지 최대 순환으로 될 수 있는 값 1,000,000보다 1 큰 값으로 초기화를 함.
    list_ = [1000001 for i in range(y + 1)]
    
    #시작 위치는 0으로 초기화
    list_[x] = 0
    
    #x~y 순환
    for i in range(x, y + 1):
        #거치지 않은 위치는 그냥 continue
        if list_[i] == 1000001:
            continue
        #i + n의 기존 값 vs 현재 위치의 값 + 1 중 작은 값으로 i + n에 값 넣어줌.
        if i + n < y + 1:
            list_[i + n] = min(list_[i + n], list_[i] + 1)
        #i * 2의 위치에 대해서 min
        if i * 2 < y + 1:
            list_[i * 2] = min(list_[i * 2], list_[i] + 1)
        #i * 3의 위치에 대해서 min
        if i * 3 < y + 1:
            list_[i * 3] = min(list_[i * 3], list_[i] + 1)
    
    #y위치의 값이 초기화가 된거면 answer로 출력
    if list_[y] != 1000001:
        answer = list_[y]
    return answer

#queue로 풀어보려 했으나 시간 초과

#from collections import deque
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