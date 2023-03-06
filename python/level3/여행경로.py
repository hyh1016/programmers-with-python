from collections import deque

answer = []

def visit(dest, start, arr, end):
    global answer
    if len(answer) == end:
        return
    if len(arr) == end:
        answer = arr[::]
        return
    if start not in dest:
        return
    N = len(dest[start])
    for _ in range(N):
        nd = dest[start].popleft()
        arr.append(nd)
        visit(dest, nd, arr, end)
        arr.pop()
        dest[start].append(nd)

        
def solution(tickets):
    global answer
    dest = {}
    for t in sorted(tickets):
        start, end = t
        if start in dest:
            dest[start].append(end)
        else:
            dest[start] = deque([end])
    first = "ICN"
    visit(dest, first, [first], len(tickets)+1)
    return answer
