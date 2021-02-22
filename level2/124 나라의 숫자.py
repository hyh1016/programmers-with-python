def solution(n):
    answer = ''
    i = 1
    while n != 0:
        mod = 3 ** i
        rest = n % mod if n % mod != 0 else mod
        number = rest // (3 ** (i-1))
        if number == 3:
            number = 4
        answer = str(number) + answer
        n -= rest
        i += 1
    return answer


# debug
print(solution(int(input())))
