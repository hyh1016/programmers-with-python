def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    for i in sorted(lost_set):
        if (1 <= i-1 <= n) and (i-1 in reserve_set):
            lost_set.remove(i)
            reserve_set.remove(i-1)
        elif (1 <= i+1 <= n) and (i+1 in reserve_set):
            lost_set.remove(i)
            reserve_set.remove(i+1)
    return n - len(lost_set)


# debug
n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))
print(solution(n, lost, reserve))
