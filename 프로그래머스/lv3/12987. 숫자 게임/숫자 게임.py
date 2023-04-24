#최대한 격차가 작은 값들로 넘는게 최대한 많이 이길 수 있다.
def solution(A, B):
    answer = 0
    
    indexA = 0
    indexB = 0
    
    #오름차순으로 정렬을 해야 각 A,B의 작은 값들끼리 비교가 가능
    A.sort()
    B.sort()
    
    #투 포인터로 B가 A보다 크면 두 인덱스를 모두 키우고
    #A가 크거나 같으면 B의 인덱스만 값을 키운다.
    while indexA < len(A) and indexB < len(B):
        if A[indexA] < B[indexB]:
            answer += 1
            indexA += 1
            indexB += 1
        elif A[indexA] >= B[indexB]:
            indexB += 1
        
    return answer