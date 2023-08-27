from collections import deque

pos_x=[0,-1,0,1]
pos_y=[-1,0,1,0]

def pop_queue(visited, maps_list, pos_queue, cur_x, cur_y):
    for i in range(4):
        if cur_x + pos_x[i] < 0 or cur_x + pos_x[i] >= len(maps_list[0]) or cur_y + pos_y[i] < 0 or cur_y + pos_y[i] >= len(maps_list):
            continue

        if (visited[cur_y+pos_y[i]][cur_x+pos_x[i]] == False) and (maps_list[cur_y+pos_y[i]][cur_x+pos_x[i]] != 'X'):
            pos_queue.append([cur_x+pos_x[i], cur_y+pos_y[i]])
            visited[cur_y+pos_y[i]][cur_x+pos_x[i]] = True
    
def solution(maps):
    answer = []
    
    maps_list = [list(i) for i in maps]
    visited = [([False] * len(maps[0])) for i in range(len(maps))]
    
    pos_queue = deque()
    
    for y in range(len(maps)):
        for x in range(len(maps[y])):
            if visited[y][x] == False and maps_list[y][x] != 'X':
                pos_queue.append([x, y])
                temp_num = 0
                while pos_queue:
                    cur_pos = pos_queue.popleft()
                    posed_x, posed_y = cur_pos[0], cur_pos[1]
                    visited[posed_y][posed_x] = True
                    temp_num += int(maps_list[posed_y][posed_x])
                    pop_queue(visited, maps_list, pos_queue, posed_x, posed_y)
                answer.append(temp_num)
                
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer