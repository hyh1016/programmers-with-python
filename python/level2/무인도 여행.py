import sys
sys.setrecursionlimit(10000)

def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(count_food(maps, i, j, visited))
    if len(answer) == 0:
        return [-1]
    return sorted(answer)

def count_food(maps, i, j, visited):
    food = int(maps[i][j])
    visited[i][j] = True
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = i+dx, j+dy
        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 'X':
            food += count_food(maps, nx, ny, visited)
    return food
