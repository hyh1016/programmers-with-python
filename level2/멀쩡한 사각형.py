from math import gcd


def solution(w, h):
    return w * h - (w + h - gcd(w, h))


# debug
w, h = map(int, input().split())
print(solution(w, h))
