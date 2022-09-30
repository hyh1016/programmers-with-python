import math


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        sqrt = math.sqrt(i)
        answer += -i if sqrt == int(sqrt) else i
    return answer


left, right = map(int, input().split())
print(solution(left, right))
