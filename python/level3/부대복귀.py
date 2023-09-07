from collections import deque

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [-1] * (n+1)
    start = destination
    distance[start] = 0
    q = deque([(start, 0)])
    visited = {start}
    
    while q:
        if len(visited) == n:
            break
        pos, dis = q.popleft()
        for p in graph[pos]:
            if p not in visited:
                distance[p] = dis+1
                visited.add(p)
                q.append((p, dis+1))
    
    answer = []
    for s in sources:
        answer.append(distance[s])
    return answer
