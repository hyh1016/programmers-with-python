import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        value = heapq.heappop(scoville)
        if value >= K:
            break
        if not scoville:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, value+second*2)
        answer += 1
    return answer


# debug
k = int(input())
scoville = list(map(int, input().split()))
print(solution(scoville, k))
