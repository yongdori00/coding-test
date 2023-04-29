def solution(sequence, k):
    answer = [0, len(sequence)]
    
    head, tail = 0, 0
    length = 0
    cur = 0
    
    while head < len(sequence) and tail < len(sequence):
        cur += sequence[tail]
        while head < tail and cur > k:
            cur -= sequence[head]
            head += 1
        
        if cur == k:
            if tail - head < answer[1] - answer[0]:
                answer[1] = tail
                answer[0] = head
            elif (tail - head) == (answer[1] - answer[0]):
                if head < answer[0]:
                    answer[1] = tail
                    answer[0] = head
        tail += 1
    return answer