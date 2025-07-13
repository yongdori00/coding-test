move = {"U":[0,1], "D":[0,-1], "R":[1, 0], "L":[-1,0]}

def moving(now, pos):
    if ( -5 <= now[0] + move[pos][0] and now[0] + move[pos][0] <= 5 ) and ( -5 <= now[1] + move[pos][1] and now[1] + move[pos][1] <= 5):
        return [now[0] + move[pos][0], now[1] + move[pos][1]]
    return now

def solution(dirs):
    answer = 0
    
    now = [0,0]
    visited = []
    
    for pos in dirs:
        after = moving(now, pos)
        if now == after:
            continue
        sort_ = sorted([now, after])
        if not sort_ in visited:
            visited.append(sort_)
        now = list(after)
    print(visited)
    return len(visited)