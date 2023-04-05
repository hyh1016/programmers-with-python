def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = 0
    camera = -30001
    for car in routes:
        start, end = car
        if start <= camera:
            continue
        camera = end
        answer += 1
    return answer
