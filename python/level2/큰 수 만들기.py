def solution(number, k):
    numbers = list(list(str(number)))
    answer = [numbers[0]]
    for i in range(1, len(numbers)):
        while k > 0 and answer and numbers[i] > answer[-1]:
            answer.pop()
            k -= 1
        else:
            answer.append(numbers[i])
    while k > 0:
        answer.pop()
        k -= 1
    return ''.join(answer)


# debug
number = input()
k = int(input())
print(solution(number, k))
