def solution(weights, head2head):
    answer = []
    for i in range(len(weights)):
        total_match = 0
        win = 0
        bigger_win = 0
        for j in range(len(head2head)):
            if head2head[i][j] == 'N':
                continue
            total_match += 1
            if head2head[i][j] == 'W':
                win += 1
                if weights[j] > weights[i]:
                    bigger_win += 1
        winning = 0
        if total_match > 0:
            winning = win/total_match
        answer.append((-winning, -bigger_win, -weights[i], i+1))
    answer.sort()
    return [i[3] for i in answer]


print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
