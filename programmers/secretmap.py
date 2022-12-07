def solution(n, arr1, arr2):
    i = 0
    answer = []
    while i < n:
        k = n - 1
        tempanswer = ''
        while k >= 0:
            if (pow(2, k) <= arr1[i]):
                tempanswer = tempanswer + '#'
                arr1[i] -= pow(2, k)
            elif (pow(2, k) > arr1[i]):
                tempanswer = tempanswer + ' '
            k -= 1
        k = n - 1
        while k >= 0:
            if (pow(2, k) <= arr2[i]):
                tempanswer = tempanswer[:n - 1 - k] + '#' + tempanswer[n - k:n]
                arr2[i] -= pow(2, k)
            k -= 1
        answer.append(tempanswer)
        i += 1
    return answer