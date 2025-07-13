def solution(n):
    answer = 0
    
    list_n = [0] * n
    
    list_n[0] = 1
    list_n[1] = 2
    
    for i in range(2, n):
        list_n[i] = (list_n[i - 2] + list_n[i - 1]) % 1000000007
        
    answer = list_n[n - 1]
    return answer