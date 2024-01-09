from collections import deque


def solution(x, y, n):
    dp = [-1] * (y+1)
    dp[x] = 0
    q = deque([x])
    while q:
        cur = q.popleft()
        if cur == y:
            return dp[cur]
        if cur + n <= y and dp[cur+n] == -1:
            dp[cur+n] = dp[cur]+1
            q.append(cur+n)
        if cur * 2 <= y and dp[cur*2] == -1:
            dp[cur*2] = dp[cur]+1
            q.append(cur*2)
        if cur * 3 <= y and dp[cur*3] == -1:
            dp[cur*3] = dp[cur]+1
            q.append(cur*3)
        
    return -1