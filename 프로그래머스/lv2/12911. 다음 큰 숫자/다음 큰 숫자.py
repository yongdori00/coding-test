def solution(n):
    answer = 0
    one_cnt = 0
    big_one_cnt = 0
    
    bin_num = bin(n)
    
    one_cnt = bin_num.count('1')
    
    while big_one_cnt != one_cnt:
        n += 1
        bin_num = bin(n)
        big_one_cnt = bin_num.count('1')
    
    answer = int(bin_num, 2)
    
    return answer