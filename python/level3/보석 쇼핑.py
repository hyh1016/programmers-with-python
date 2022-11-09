def solution(gems):
    answer = []
    types = set(gems)
    count = dict()
    
    start = 0
    for i in range(len(gems)):
        gem = gems[i]
        if gem in count:
            count[gem] += 1
        else:
            count[gem] = 1
        if gems[start] == gem:
            while True:
                g = gems[start]
                if count[g] < 2:
                    break
                count[g] -= 1
                start += 1
        if len(types) == len(count):
            answer.append((i-start+1, start, i))

    answer.sort()
    return [answer[0][1]+1, answer[0][2]+1]
