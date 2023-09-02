from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    start = 0
    lever = 0
    end = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)

    start_to_lever = min_time(maps, start, lever)
    if start_to_lever == -1:
        return -1
    lever_to_end = min_time(maps, lever, end)
    if lever_to_end == -1:
        return -1
    return start_to_lever + lever_to_end


def min_time(maps, start, end):
    N = len(maps)
    M = len(maps[0])
    visited = [[False] * M for _ in range(N)]
    visited[start[0]][start[1]] = True
    q = deque([(start[0], start[1], 0)])
    while q:
        cr, cc, time = q.popleft()
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] != 'X' and not visited[nr][nc]:
                visited[nr][nc] = True
                if nr == end[0] and nc == end[1]:
                    return time+1
                q.append((nr, nc, time+1))
    return -1