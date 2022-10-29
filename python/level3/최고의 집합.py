def solution(n, s):
    if n > s:
        return [-1]
    num = s//n
    big_count = s%n
    small_count = n - (s%n)
    return [num]*small_count + [num+1]*big_count


print(solution(2, 9)) # [4, 5]
