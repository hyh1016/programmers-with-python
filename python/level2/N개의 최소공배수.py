def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a*b) // gcd(a, b)

def solution(arr):
    arr.sort()
    current_lcm = lcm(arr[0], arr[1])
    for i in range(2, len(arr)):
        current_lcm = lcm(current_lcm, arr[i])
    return current_lcm


# debug
print(solution(list(map(int, input().split()))))
