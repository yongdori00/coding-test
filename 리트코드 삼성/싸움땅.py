dx = [0,1,0,-1]
dy = [-1,0,1,0]

def move(x, y, d):
    return dx[d] + x, dy[d] + y

def get_weapon(weapon_, map_, man_index, moved_x, moved_y):
    if weapon_[man_index] < map_[moved_y][moved_x]:
        temp = weapon_[man_index]
        weapon_[man_index] = map_[moved_y][moved_x]
        map_[moved_y][moved_x] = temp

def result(winner_index, loser_index, weapon_, map_, x, y, answer):
    map_[x][y] = weapon_[loser_index]
    weapon_[loser_index] = 0
    answer[winner_index] += 1
    print(answer)
    return loser_index
def wall(x, y, d, n):
    if not (0 <= x + dx[d] and x + dx[d] < n) or not (0 <= y + dy[d] and y + dy[d] < n):
        return True
    return False

def man_wall(x, y, d, map_man):
    if map_man[y + dy[d]][x + dx[d]] != -1:
        return True
    return False

def loser_wall(loser_index, map_man, man_inf):
    man_x = man_inf[loser_index][1]
    man_y = man_inf[loser_index][0]
    man_d = man_inf[loser_index][2]
    #벽에 만났을 때
    if wall(man_x, man_y, man_d, len(map_man)):
        return True
    #사람을 만났을 때
    if man_wall(man_x, man_y, man_d, map_man):
        return True
    return False

n, m, k = map(int, input().split())

#무기의 위치
map_ = []
#실제 사람이 있는 위치에 대한 map
map_man = [[-1 for i in range(n)]for i in range(n)]
#사람에 대한 정보
man_inf = []
#사람이 가지고 있는 무기의 공격력
weapon_ = [0 for i in range(m)]
answer = [0 for i in range(m)]

for i in range(n):
    map_.append(list(map(int, input().split())))

for i in range(m):
    man_inf.append(list(map(int, input().split())))
    man_inf[i][0] -= 1
    man_inf[i][1] -= 1
    map_man[man_inf[i][0]][man_inf[i][1]] = i

for i in range(k):
    for j in range(m):
        #우선 이동을 하려 한다. 앞이 벽이면 True return
        wall_ = wall(man_inf[j][1], man_inf[j][0], man_inf[j][2], n)
        if wall_:
            #방향 전환
            man_inf[j][2] = (man_inf[j][2] + 2) % 4

        #벽이 아니면 사람을 만나든 총을 줍든 해야함.
        #이동
        cur_index = map_man[man_inf[j][0]][man_inf[j][1]]
        map_man[man_inf[j][0]][man_inf[j][1]] = -1
        moved_x, moved_y = move(man_inf[j][1], man_inf[j][0], man_inf[j][2])

        # print(map_man)
        # print(moved_x, moved_y)
        print(map_)

        #이동할 자리에 사람이 있는지
        if map_man[moved_y][moved_x] != -1:
            loser_index = -1
            #새로 들어온 사람이 더 약할 때
            if man_inf[cur_index][3] + weapon_[cur_index] < man_inf[map_man[moved_y][moved_x]][3] + weapon_[map_man[moved_y][moved_x]]:
                loser_index = result(map_man[moved_y][moved_x], cur_index, weapon_, map_, moved_x, moved_y, answer)
            #기존이 더 약할 때
            elif man_inf[cur_index][3] + weapon_[cur_index] > man_inf[map_man[moved_y][moved_x]][3] + weapon_[map_man[moved_y][moved_x]]:
                loser_index = result(cur_index, map_man[moved_y][moved_x], weapon_, map_, moved_x, moved_y, answer)
            #합이 같을 떄
            else:
                #새로온 사람의 초기가 더 약할 때
                if man_inf[cur_index][3] < man_inf[map_man[moved_y][moved_x]][3]:
                    loser_index = result(map_man[moved_y][moved_x], cur_index, weapon_, map_, moved_x, moved_y, answer)
                #기존의 초기가 더 약할 때
                else:
                    loser_index = result(cur_index, map_man[moved_y][moved_x], weapon_, map_, moved_x, moved_y, answer)

            #이동해서 들어간 사람의 위치 값 업데이트
            man_inf[cur_index][1] = moved_x
            man_inf[cur_index][0] = moved_y

            #진 사람이 벽이나 사람을 새로 만나면 빙글 돎.
            while loser_wall(loser_index, map_man, man_inf):
                # print(map_man, moved_x, moved_y)
                man_inf[loser_index][2] = (man_inf[loser_index][2] + 1) % 4

            man_inf[loser_index][1], man_inf[loser_index][0] = move(man_inf[loser_index][1], man_inf[loser_index][0], man_inf[loser_index][2])
            map_man[man_inf[loser_index][0]][man_inf[loser_index][1]] = loser_index
            # print(man_inf[loser_index][1], man_inf[loser_index][0])
            #무기 줍기
            get_weapon(weapon_, map_, loser_index, man_inf[loser_index][1], man_inf[loser_index][0])

        else:
            #땅 무기가 더 강하면 줍줍
            get_weapon(weapon_, map_, j, moved_x, moved_y)
            #그 위치에 사람이 있음.
            map_man[moved_y][moved_x] = j

print(answer)
