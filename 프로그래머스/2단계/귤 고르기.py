def solution(k, tangerine):
    answer = 0
    num_dict = dict()
    
    # 각 수마다 갯수를 파악하는 것이 중요했다.
    for i in tangerine:
        num_dict[i] = num_dict.get(i, 0) + 1
    
    # 갯수 단위로 내림차순 정렬을 해야 갯수가 많은 것부터 빼서 최소를 만들 수 있었다.
    num_dict = sorted(num_dict.items(), key = lambda x:x[1], reverse = True)
    
    # k가 0보다 클 동안 돌리면 됨.
    for i in num_dict:
        if k > 0:
            k -= i[1]
            answer += 1
        elif k <= 0:
            break
    
    return answer