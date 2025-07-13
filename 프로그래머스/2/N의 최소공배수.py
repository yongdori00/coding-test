#최대 공약수 구하는 메소드
def gcd(num1, num2):
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    
    return num1

def solution(arr):
    answer = 0
    temp_answer = 1
    
    for i in range(len(arr)):
        #임시 답과 현재 요소간의 최대 공약수 구하기
        temp_gcd = gcd(arr[i], temp_answer)
        #각 값의 곱
        temp_answer = arr[i] * temp_answer // temp_gcd 
    
    answer = temp_answer
    return answer