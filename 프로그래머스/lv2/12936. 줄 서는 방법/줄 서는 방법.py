#permutation 시간 초과
def dp(n, k, visited, answer, num):
    cnt = 0
    nk = 1
    
    for i in range(1, len(visited)):
        if visited[i] == False:
            cnt += 1
            
    #False의 갯수 - 1 만큼 factorial을 만들어줌.
    #nk가 주기가 될겅.ㅁ
    for i in range(1, cnt):
        nk *= i

    #dp
    #k보다 작으면서 최대 값일 때 dp를 한번 더 들어감.
    #break 안해줘도 dp로 들어가면서 visited가 전부 True로 바뀌어 있을 에정이기 때문
    for i in range(1, len(visited)):
        if visited[i] == True:
            continue
        if k > num + nk:
            num += nk
        else:
            visited[i] = True
            answer.append(i)
            dp(n, k, visited, answer, num)
            break
        

def solution(n, k):
    answer = []
    visited = [False for i in range(n + 1)]
    
    dp(n, k, visited, answer, 0)
    
    return answer