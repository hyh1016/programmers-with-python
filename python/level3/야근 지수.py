def solution(n, works):
    result = 0
    count = dict()
    for w in works:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1
    biggest = max(count.keys())
    for i in range(biggest, 0, -1):
        cnt = count[i]
        minus = cnt if n > cnt else n
        count[i] -= minus
        if i-1 in count:
            count[i-1] += minus
        else:
            count[i-1] = minus
        n -= minus
        if n == 0:
            break
    if n > 0:
        return 0
    for k, v in count.items():
        if v == 0:
            continue
        result += (k**2) * v
    return result


print(solution(4, [4, 3, 3])) # 12
