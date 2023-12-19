def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [(0, numbers[0])]
    for i in range(1, len(numbers)):
        while stack:
            oi, on = stack[-1]
            if on < numbers[i]:
                answer[oi] = numbers[i]
                stack.pop()
            else:
                break
        stack.append((i, numbers[i]))
    return answer