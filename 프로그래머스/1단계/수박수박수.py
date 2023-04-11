def solution(n):
    answer = ''
    arrlist = []
    for i in range(n):
        if i % 2 == 0:
            arrlist.append('수')
        else:
            arrlist.append('박')
            
    answer = ''.join(arrlist)
    
    return answer