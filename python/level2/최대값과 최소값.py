def solution(s):
    numbers = list(map(int, s.split(' ')))
    return str(min(numbers)) + ' ' + str(max(numbers))

#debug
# example: "3 1 4 2"
print(solution(input()))
