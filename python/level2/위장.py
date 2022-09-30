def solution(clothes):
    hash = {}
    for i in clothes:
        if hash.get(i[1]):
            hash[i[1]] += 1
        else:
            hash[i[1]] = 1
    answer = 1
    for i in hash.values():
        answer *= (i + 1)
    return answer - 1


# debug
n = int(input())
clothes = [input().split() for _ in range(n)]
print(solution(clothes))
