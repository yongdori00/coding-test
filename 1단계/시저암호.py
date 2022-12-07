def solution(s, n):
    answer = ''
    capitallist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphalist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    lists = list(s)
    
    for i in range(len(lists)):
        k = 0
        if lists[i] in capitallist:
            k = capitallist.index(lists[i])    
            k = (k + n) % 26
            lists[i] = capitallist[k]
        elif lists[i] in alphalist:
            k = alphalist.index(lists[i])
            k = (k + n) % 26
            lists[i] = alphalist[k]
            
            
    answer = ''.join(lists)
    return answer