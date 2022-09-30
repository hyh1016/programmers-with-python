from collections import deque


def solution(people, limit):
    q = deque(sorted(people))
    answer = 0
    while q:
        answer += 1
        total = q.pop()
        while q and total + q[0] <= limit:
            total += q.popleft()
    return answer


# debug
limit = int(input())
people = list(map(int, input().split()))
print(solution(people, limit))
