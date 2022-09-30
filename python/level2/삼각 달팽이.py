def solution(n):
    tri = [[0] * (i + 1) for i in range(n)]
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    tri[0][0] = 1
    y, x = 0, 0
    number = 2
    move = 0
    for i in range(n):
        nx, ny = x + dx[move], y + dy[move]
        while 0 <= ny < len(tri) and 0 <= nx < len(tri[ny]) and tri[ny][nx] == 0:
            y, x = ny, nx
            tri[y][x] = number
            number += 1
            nx, ny = x + dx[move], y + dy[move]
        move = (move + 1) % 3

    return [j for i in tri for j in i]


# debug
print(solution(int(input())))
