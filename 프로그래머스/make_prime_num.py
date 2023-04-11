from itertools import combinations

def solution(nums):
    answer = 0
    nums.sort()
    max_num = nums[-1] + nums[-2] + nums[-3]
    min_num = nums[0] + nums[1] + nums[2]
    prime_array = []
    is_prime = False

    new_arrays = list(combinations(nums, 3))
    new_sum_arrays = []

    for i in new_arrays:
        new_sum_arrays.append(sum(i))

    for i in range(min_num, max_num + 1):
        is_prime = True
        j = 2
        while j * j <= i:
            if i % j == 0:
                is_prime = False
                break
            j += 1
            
        if is_prime == True:
            prime_array.append(i)

    for i in new_sum_arrays:
        if i in prime_array:
            answer += 1

    return answer

solution([1,2,13])