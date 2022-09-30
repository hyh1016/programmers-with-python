def solution(board, moves):
    nboard = [[]]
    for i in range(len(board)):
        col = []
        for j in range(len(board)):
            if board[len(board)-j-1][i] != 0:
                col.append(board[len(board)-j-1][i])
        nboard.append(col)
    answer = 0
    stack = []
    for i in moves:
        if nboard[i]:
            value = nboard[i].pop()
            if stack and stack[-1] == value:
                stack.pop()
                answer += 2
            else:
                stack.append(value)

    return answer


# debug
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))
print(solution(board, moves))
