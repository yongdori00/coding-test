def solution(arr1, arr2):
    answer = [([0] * len(arr2[0])) for i in range(len(arr1))]
    
    # 각 행렬의 외측 길이를 확인
    # 내측 길이를 for로 돌면서 각 행렬의 외측 좌표들의 합을 계산
    for arr1_index in range(len(arr1)):
        for arr2_index in range(len(arr2[0])):
            inner_answer = []
            for inner_index in range(len(arr2)):
                answer[arr1_index][arr2_index] += arr1[arr1_index][inner_index] * arr2[inner_index][arr2_index]

    return answer