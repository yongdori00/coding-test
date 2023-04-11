def solution(nums):
    answer = 0
    new_array = []
    length = len(nums) / 2

    for ele in nums:
        if ele in new_array:
            continue
        else:
            new_array.append(ele)

    if length > len(new_array):
        answer = len(new_array)
    else:
        answer = length
    
    return answer