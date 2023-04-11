def solution(people, limit):
    answer = 0
    front = 0
    rear = len(people) - 1
    cur = 0
    
    people.sort(reverse = True)
    
    while front <= rear:
        if cur == 0:
            cur += people[front]
            if front < rear and cur + people[rear] > limit:
                answer += 1
                cur = 0
            front += 1

        elif cur != 0 and cur + people[rear] <= limit:
            cur += people[rear]
            if front < rear and cur + people[rear] > limit:
                answer += 1
                cur = 0
            rear -= 1
        
        if front == rear:
            front += 1
            answer += 1

    return answer