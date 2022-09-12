def solution(brown, yellow):
    # x*y = 노란색 개수
    # 2x+2y+4 = 갈색 개수
    # x > y
    # answer = [x+2, y+2]
    for x in range(1, 2500):
        for y in range(1, x+1):
            if x * y == yellow and x+y+2 == brown//2:
                return [x+2, y+2]


# debug
brown, yellow = map(int, input().split())
print(solution(brown, yellow))
