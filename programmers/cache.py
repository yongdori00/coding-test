def solution(cacheSize, cities):
    answer = 0
    cache = []

    for i in cities:
        i = i.lower()
        if cacheSize == 0:
            answer+=5
        elif i not in cache:
            if len(cache) < cacheSize:
                cache.append(i)
                answer+=5
            else:
                cache.pop(0)
                cache.append(i)
                answer+=5
        else:
            cache.pop(cache.index(i))
            cache.append(i)
            answer+=1

    return answer

print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))