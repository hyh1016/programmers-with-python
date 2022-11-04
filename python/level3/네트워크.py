def dfs(computers, c, visited):
    visited[c] = True
    for i in range(len(computers)):
        if computers[c][i] == 1 and not visited[i]:
            dfs(computers, i, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            answer += 1
    return answer
