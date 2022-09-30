from collections import deque


def solution(bridge_length, weight, truck_weights):
    q = deque([(truck_weights.pop(), bridge_length + 1)])
    time = 1
    next = truck_weights.pop() if truck_weights else None
    while q:
        time += 1
        if q[0][1] == time:
            q.popleft()
        sum_weights = sum(i[0] for i in q)
        if next and sum_weights + next <= weight:
            q.append((next, time + bridge_length))
            next = truck_weights.pop() if truck_weights else None

    return time


# debug
bridge_length, weight = map(int, input().split())
truck_weights = list(map(int, input().split()))
print(solution(bridge_length, weight, truck_weights))
