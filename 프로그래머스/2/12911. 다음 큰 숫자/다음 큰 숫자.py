#법칙을 찾으려고 하다 보니 한참 걸렸는데
#그냥 하나씩 늘려가면서 1의 갯수만 같으면 되는거였음.
def solution(n):
    one_cnt = 0
    big_one_cnt = 0
    
    #초기 값의 1의 갯수
    bin_num = bin(n)
    one_cnt = bin_num.count('1')
    
    #늘려가면서 1의 갯수를 찾음
    while big_one_cnt != one_cnt:
        n += 1
        bin_num = bin(n)
        big_one_cnt = bin_num.count('1')
    
    return int(bin_num, 2)