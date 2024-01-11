def solution(scores):
    answer = 1
    wanho = scores[0]
    wanho_sum = sum(scores[0])
    scores.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    max_score = 0
    for s in scores:
        ssum = sum(s)
        if s[1] >= max_score:
            max_score = s[1]
            if ssum > wanho_sum:
                answer += 1
        else:
            if s == wanho:
                return -1
    return answer