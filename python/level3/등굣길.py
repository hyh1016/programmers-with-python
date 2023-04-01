def solution(m, n, puddles):
    MOD = 1000000007
    graph = [[0] * m for _ in range(n)]
    for p in puddles:
        c, r = p
        graph[r-1][c-1] = -1
    graph[0][0] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == -1:
                continue
            if i > 0 and graph[i-1][j] > 0:
                graph[i][j] += graph[i-1][j] % MOD
            if j > 0 and graph[i][j-1] > 0:
                graph[i][j] += graph[i][j-1] % MOD
    return graph[n-1][m-1] % MOD