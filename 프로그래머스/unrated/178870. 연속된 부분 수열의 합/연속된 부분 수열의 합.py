def solution(sequence, k):
    answer = [0, len(sequence)]
    
    #head, tail, 합의 인덱스 길이, 현재 합
    head, tail = 0, 0
    length = 0
    cur = 0
    
    #sequence끝 전까지
    while head < len(sequence) and tail < len(sequence):
        #일단 다음 값 더하기
        cur += sequence[tail]
        #처음 위치 값을 빼도 k보다 클 경우에는 계속 뺌
        while head < tail and cur > k:
            cur -= sequence[head]
            head += 1
        
        #k랑 같은 경우
        if cur == k:
            #일반적인 경우에는 업데이트
            if tail - head < answer[1] - answer[0]:
                answer[1] = tail
                answer[0] = head
            #기존의 length와 길이가 같다면
            elif (tail - head) == (answer[1] - answer[0]):
                if head < answer[0]:
                    answer[1] = tail
                    answer[0] = head
        #꼬리는 무조건 한 사이클에 한칸씩 이동
        tail += 1
    return answer