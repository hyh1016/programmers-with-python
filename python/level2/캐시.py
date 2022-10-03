from collections import deque


def solution(cacheSize, cities):
    answer = 0
    
    # no cache
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = deque()
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
    return answer


# for debug
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
