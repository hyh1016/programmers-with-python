answer = 0
cost_info = {
    'diamond': [1, 5, 25],
    'iron': [1, 1, 5],
    'stone': [1, 1, 1]
}


def pick(minerals, current, picks, status):
    global answer
    if len(minerals) < current or sum(picks) == 0:
        answer = min(answer, status)
        return
    
    for i in range(len(picks)):
        p = picks[i]
        if p < 1:
            continue
        cost = 0
        for j in range(5):
            if not len(minerals) > current+j:
                break
            t = minerals[current+j]
            cost += cost_info[t][i]
        picks[i] -= 1
        pick(minerals, current+5, picks, status+cost)
        picks[i] += 1


def solution(picks, minerals):
    global answer
    answer = 25 * len(minerals)
    dia, iron, stone = picks
    pick(minerals, 0, picks, 0)
    return answer
