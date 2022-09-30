MAX = 100000
MOD = 1234567


def solution(n):
    dp = [0] * (MAX + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    return dp[n]


print(solution(int(input())))
