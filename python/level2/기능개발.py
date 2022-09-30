from collections import deque


def solution(progresses, speeds):
    q = deque([[progresses[i], speeds[i]] for i in range(len(progresses))])
    answer = []
    while q:
        for i in q:
            i[0] += i[1]
        if q[0][0] >= 100:
            count = 0
            while q[0][0] >= 100:
                q.popleft()
                count += 1
                if not q:
                    break
            answer.append(count)

    return answer


progresses = list(map(int, input().split()))
speeds = list(map(int, input().split()))
print(solution(progresses, speeds))
