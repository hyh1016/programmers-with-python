def solution(numbers):
    answer = []
    for num in numbers:
        reverse = 0
        div = num
        while div != 0:
            if div % 2 == 0:
                break
            div //= 2
            reverse += 1
        fnum = num + (2**(reverse)) - (2**(reverse-1) if reverse > 0 else 0)
        answer.append(fnum)
    return answer


print(solution(list(map(int, input().split()))))
