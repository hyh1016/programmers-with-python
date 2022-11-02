answer = set()

def backtracking(candidate, result):
    global answer
    if len(result) == len(candidate):
        answer.add(''.join(sorted(result)))
        return

    for c in candidate[len(result)]:
        if str(c) in result:
            continue
        result.add(str(c))
        backtracking(candidate, result)
        result.remove(str(c))

def solution(user_id, banned_id):
    candidate = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        bid = banned_id[i]
        for j in range(len(user_id)):
            uid = user_id[j]
            if len(bid) != len(uid):
                continue
            is_candidate = True
            for k in range(len(bid)):
                if bid[k] == '*':
                    continue
                if bid[k] != uid[k]:
                    is_candidate = False
                    break
            if is_candidate:
                candidate[i].append(j)
    backtracking(candidate, set())
    return len(answer)
