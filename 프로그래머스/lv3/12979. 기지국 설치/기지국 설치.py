def solution(n, stations, w):
    answer = 0
        
    for i in range(len(stations)):
        if i == 0 and stations[0] - w > 1:
            answer += (stations[i] - w - 1) // (2 * w + 1)
            if (stations[i] - w - 1) % (2 * w + 1) != 0:
                answer += 1
            
        if i == len(stations) - 1 and stations[i] + w < n:
            answer += (n - stations[i] - w) // (2 * w + 1)
            if (n - stations[i] - w) % (2 * w + 1) != 0:
                answer += 1
            break
            
        if len(stations) != 1 and i < len(stations) - 1:
            if stations[i + 1] - stations[i] - 2 * w - 1 > 0:
                answer += (stations[i + 1] - stations[i] - 2 * w - 1) // (2 * w + 1)
                if (stations[i + 1] - stations[i] - 2 * w - 1) % (2 * w + 1) != 0:
                    answer += 1

    return answer