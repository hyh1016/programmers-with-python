from itertools import permutations


def solution(numbers):
    MAX = int(1e7)
    number_list = list(numbers)
    prime = [True] * MAX
    prime[0] = prime[1] = False
    for i in range(2, MAX):
        if prime[i]:
            for j in range(2*i, MAX, i):
                prime[j] = False
    candidate = set()
    for i in range(1, len(number_list) + 1):
        for i in list(permutations(number_list, i)):
            if i[0] != 0:
                candidate.add(int(''.join(i)))
    answer = 0
    for i in candidate:
        if prime[i]:
            answer += 1
    return answer
