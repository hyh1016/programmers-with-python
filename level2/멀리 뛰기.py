def solution(n):
    case = [0] * (n+1)
    case[0] = case[1] = 1
    for i in range(2, n+1):
        case[i] = (case[i-1] + case[i-2]) % 1234567
    return case[n]


# debug
print(solution(int(input())))
