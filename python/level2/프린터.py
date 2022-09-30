from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque([(priorities[i], i) for i in range(len(priorities))])
    while q:
        is_max = True
        if q[0][0] < 9:
            for i in range(len(q)):
                if q[i][0] > q[0][0]:
                    is_max = False
                    break
        current = q.popleft()
        if is_max:
            answer += 1
            if current[1] == location:
                break
        else:
            q.append(current)

    return answer


# debug
location = int(input())
priorities = list(map(int, input().split()))
print(solution(priorities, location))
