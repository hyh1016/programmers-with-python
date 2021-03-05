def solution(skill, skill_trees):
    answer = 0
    s = list(skill)
    s_set = set(list(skill))
    for i in skill_trees:
        next = 0
        is_valid = True
        for j in i:
            if j in s_set:
                if j == s[next]:
                    next += 1
                else:
                    is_valid = False
                    break
        if is_valid:
            answer += 1
    return answer


# debug
print(solution(input(), input().split()))
