def solution(n, left, right):
    answer = []

    height = 0
    width = 0

    height = left // n + 1
    width = left % n + 1

    # 가로 인덱스, 세로 인덱스를 놓고 가로 인덱스가 세로 인덱스보다 작으면
    # 무조건 세로 인덱스의 값이 들어가게함.
    # 행을 넘어가게 되면 가로 인덱스를 1로 초기화, 세로 인덱스를 한 칸 추가
    while left <= right:
        if width <= height:
            answer.append(height)
        else:
            answer.append(width)

        if width % n == 0:
            width = 0
            height += 1

        width += 1

        left += 1


    return answer