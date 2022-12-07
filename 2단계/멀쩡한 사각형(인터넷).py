def gcd(w, h):
    while w % h != 0:
        temp = h
        h = w % h
        w = temp
    
    return h

def solution(w,h):
    answer = 1
    
    gcdNum = gcd(w, h)

    empty_square = w // gcdNum + h // gcdNum - 1

    answer = w * h - gcdNum * empty_square

    return answer
