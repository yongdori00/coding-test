def solution(A, B):
    answer = 0
    
    indexA = 0
    indexB = 0
    
    A.sort()
    B.sort()
    
    while indexA < len(A) and indexB < len(B):
        if A[indexA] < B[indexB]:
            answer += 1
            indexA += 1
            indexB += 1
        elif A[indexA] >= B[indexB]:
            indexB += 1
        
    return answer