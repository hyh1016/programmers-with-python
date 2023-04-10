from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n)]
    for a, b in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    visited = [False] * n
    distances = [0] * n
    q = deque([(0, 0)])
    while q:
        node, dist = q.popleft()
        if visited[node]:
            continue
        visited[node] = True
        distances[dist] += 1
        for i in graph[node]:
            q.append((i, dist+1))
    
    for i in range(len(distances)-1, 0, -1):
        if distances[i] != 0:
            return distances[i]