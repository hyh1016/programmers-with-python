def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer


# debug
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solution(A, B))
