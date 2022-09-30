def solution(s):
    answer = True
    left = 0
    right = 0
    for i in s:
        if i == '(':
            left += 1
        elif i == ')':
            right += 1
        if right > left:
            answer = False
            break
    if left != right:
        answer = False
    return answer

# debug
s = '(())'
print(solution(s)) # True

# debug
s = '())('
print(solution(s)) # False
