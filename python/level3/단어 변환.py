answer = 51

def dfs(words, current, target, count, visited):
    global answer
    if current == target:
        answer = min(answer, count)
        return
    for word in words:
        if word in visited:
            continue
        diff = 0
        for i in range(len(word)):
            if current[i] != word[i]:
                diff += 1
            if diff > 2:
                break
        if diff == 1:
            visited.add(word)
            dfs(words, word, target, count+1, visited)
            visited.remove(word)

def solution(begin, target, words):
    global answer
    dfs(words, begin, target, 0, set())
    if answer == 51:
        return 0
    return answer
