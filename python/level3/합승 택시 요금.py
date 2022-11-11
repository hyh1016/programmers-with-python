def solution(n, s, a, b, fares):
    INF = n * 100000
    
    dist = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        dist[i][i] = 0
    for f in fares:
        i, j, w = f
        dist[i][j] = w
        dist[j][i] = w
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    
    answer = INF * 2
    for i in range(1, n+1):
        result = dist[s][i] + dist[i][a] + dist[i][b]
        answer = min(answer, result)
    return answer
