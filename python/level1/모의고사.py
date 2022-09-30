def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = [0] * 3
    for i, v in enumerate(answers):
        if one[i % len(one)] == v:
            correct[0] += 1
        if two[i % len(two)] == v:
            correct[1] += 1
        if three[i % len(three)] == v:
            correct[2] += 1
    max_correct = max(correct)
    answer = []
    for i in range(len(correct)):
        if max_correct == correct[i]:
            answer.append(i+1)
    return answer


# debug
answers = list(map(int, input().split()))
print(solution(answers))
