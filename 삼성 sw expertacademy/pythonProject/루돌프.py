# 이동 방향 상하좌우
left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1, 0)

# 이동 방향 대각선
# l_up = (-1, -1)
# r_up = (-1, 1)
# l_down = (1, -1)
# r_down = (1, 1)



''' main에서 호출하는 methods '''
def update_map(santa_pos, ludolf_pos, whole_map):
    # 루돌프의 위치 초기화 (루돌프는 -1이다.)
    whole_map[ludolf_pos[0]][ludolf_pos[1]] = -1
    # 산타의 위치 초기화 (산타는 각 번호로 저장한다.)
    for pos in range(1, len(santa_pos)):
        whole_map[pos[1]][pos[2]] = pos[0]

'''현재까지는 움직임에 대한 크기만 구현 했음. 실제 움직임 X'''
# 루돌프 움직임
def ludolf_turn(santa_pos, ludolf_pos, whole_map):
    direction = [0,0]
    ludolf = False
    santa_num, dis = find_santa(ludolf_pos, santa_pos)

    # 루돌프는 대각선도 가능하기 때문에 상하, 좌우를 각각 한번씩 조건으로 넣는다.
    if santa_pos[santa_num][0] > ludolf_pos[0]:
        direction[0] += 1
    elif santa_pos[santa_num][0] < ludolf_pos[0]:
        direction[0] -= 1

    if santa_pos[santa_num][1] > ludolf_pos[1]:
        direction[1] += 1
    elif santa_pos[santa_num][1] < ludolf_pos[1]:
        direction[1] -= 1

    move(direction, santa_pos, ludolf_pos, ludolf)

# 산타 움직임
# 루돌프는 한 마리 이기 때문에 굳이 제일 가까운걸 찾을 필요 없어서 find_ludolf 함수 필요 x
def santa_turn(santa_pos, ludolf_pos, whole_map):
    for santa_num in range(1, len(santa_pos)):
        direction = [0, 0]
        santa = True

        # 산타는 상하좌우 다 해서 한번만 가능하기 때문
        if santa_pos[santa_num][0] < ludolf_pos[0]:
            direction[0] += 1
            # 여기 조건문들에 산타가 이미 있을 때를 조건 처리 해주어야 함.
        elif santa_pos[santa_num][0] > ludolf_pos[0]:
            direction[0] -= 1
        elif santa_pos[santa_num][1] < ludolf_pos[1]:
            direction[1] += 1
        elif santa_pos[santa_num][1] > ludolf_pos[1]:
            direction[1] -= 1

        move(direction, santa_pos, ludolf_pos, santa)

# 기절 상태 확인
def check_sleep():
    pass

# 최종 점수
def finish():
    pass

''' method에서 호출하는 methods '''
# 충돌
def crash():
    pass

# 상호작용
def push_santa():
    pass

# 기절
def sleep():
    pass

# 산타를 찾는 함수
def find_santa(ludolf_pos, santa_pos):
    near_santa, near_dis = -1, 10000
    for i in range(1, len(santa_pos)):
        cur_dis = cal_dis(ludolf_pos, santa_pos[i])
        # 더 가까운 곳
        if cur_dis < near_dis:
            near_santa = i
            near_dis = cur_dis
        # 거리가 같으 면
        elif cur_dis == near_dis:
            # r이 큰 곳
            if santa_pos[i][0] > santa_pos[near_santa][0]:
                near_santa = i
                near_dis = cur_dis
            # r이 같으면 c가 큰 곳
            elif santa_pos[near_santa][0] == santa_pos[near_santa][0]:
                if santa_pos[near_santa][1] < santa_pos[near_santa][1]:
                    near_santa = i
                    near_dis = cur_dis

    return near_santa, near_dis

# 거리 측정 (r1-r2)^2 + (c1-c2)^2
def cal_dis(ludolf_pos, santa_pos):
    dis = ( (ludolf_pos[0] - santa_pos[0]) ** 2 ) + ( (ludolf_pos[1] - santa_pos[1]) ** 2 )
    return dis

# 대상을 움직이는 method
# direction(방향 배열), santa_pos, ludolf_pos, who(True면 산타, False면 루돌프)
def move(direction, santa_pos, ludolf_pos, who):



def main():
    # 첫 입력
    N, M, P, C, D = map(int, input().split())

    # 산타, 루돌프의 위치를 맵 위에 위치
    whole_map = [[0 for i in range(P + 1)] for j in range(P + 1)]
    print(whole_map)
    # 기절한 산타의 남은 턴
    sleep_santa = [0 for i in range(P)]
    # 산타의 점수
    point_santa = [0 for i in range(P)]

    # 산타, 루돌프 위치
    santa_pos = [0 for i in range(P+1)]
    ludolf_pos = list(map(int, input().split()))

    # 산타 위치 입력 (산타의 위치 정보는 [번호, 세로, 가로]로 저장된다.)
    for i in range(P):
        num, row, col = map(int, input().split())
        santa_pos[num] = [row, col]

    # 최초의 맵을 초기화 한다.
    update_map(santa_pos, ludolf_pos, whole_map)

    # 턴을 반복한다.
    for turn in range(M):
        # 루돌프의 이동 차례
        ludolf_turn(santa_pos, ludolf_pos, whole_map)
        # 산타의 이동 차례 이전 기절 상태 확인

        # 산타의 이동 차례
        santa_turn(santa_pos, ludolf_pos, whole_map)

if __name__ == "__main__":
    main()
