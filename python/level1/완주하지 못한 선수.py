def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


# debug
participant = list(input().split())
completion = list(input().split())
print(solution(participant, completion))
