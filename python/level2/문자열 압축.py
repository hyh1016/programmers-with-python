def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        ns = ''
        cnt = 1
        prev = s[:i]
        for j in range(i, len(s), i):
            if prev == s[j:j+i]:
                cnt += 1
            else:
                ns += (str(cnt) if cnt > 1 else '') + prev
                prev = s[j:j+i]
                cnt = 1
        ns += (str(cnt) if cnt > 1 else '') + prev
        answer = min(answer, len(ns))
    return answer


# debug
print(solution(input()))
