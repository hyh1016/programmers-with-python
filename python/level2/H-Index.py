def solution(citations):
    citations.sort()
    answer = 0
    for i in range(1, len(citations) + 1):
        if citations[len(citations)-i] >= i:
            answer = i
    return answer


# debug
citations = list(map(int, input().split()))
print(solution(citations))
