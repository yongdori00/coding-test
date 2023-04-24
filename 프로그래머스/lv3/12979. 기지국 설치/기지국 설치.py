#브루트 포스를 생각했으나 연산수를 보고 최적화 방법을 고민함.
#W의 길이 * 2 + 1을 수학으로 활용할 방법 없나 고민함.
def solution(n, stations, w):
    answer = 0
    
    #크게 세 영역으로 나눔.
    #1. 첫번째 이전
    #2. 첫번째 ~ 마지막
    #3. 마지막 이후
    #기지국을 최소로 놓는 갯수는 (인덱스 간격 - 1 - (2 * w))에 대해서 (2 * w + 1)로 나눈 몫 + (나머지가 0 이 아닐 경우 1)
    for i in range(len(stations)):
        #첫번째 이전 영역(1부터라고 첫번째 인덱스까지라고 생각)
        if i == 0 and stations[0] - w > 1:
            answer += (stations[i] - w - 1) // (2 * w + 1)
            if (stations[i] - w - 1) % (2 * w + 1) != 0:
                answer += 1
        
        #마지막 이후 영역(마지막 인덱스부터 n까지라고 생각)
        if i == len(stations) - 1 and stations[i] + w < n:
            answer += (n - stations[i] - w) // (2 * w + 1)
            if (n - stations[i] - w) % (2 * w + 1) != 0:
                answer += 1
            break
            
        #사이 영역
        #요소가 하나일 경우에는 그 요소만으로 첫번째이자, 마지막이 될 수 있고 그 사이 영역은 필요 없어짐.
        if len(stations) != 1 and i < len(stations) - 1:
            if stations[i + 1] - stations[i] - 2 * w - 1 > 0:
                answer += (stations[i + 1] - stations[i] - 2 * w - 1) // (2 * w + 1)
                if (stations[i + 1] - stations[i] - 2 * w - 1) % (2 * w + 1) != 0:
                    answer += 1

    return answer