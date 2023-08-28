def solution(sequence, k):
    answer = [0, len(sequence)]
    start, end = 0, 0
    total = sequence[0]
    while end >= start:
        if total > k:
            total -= sequence[start]
            start += 1
            continue
        if k == total:
            if answer[1] - answer[0] > end - start:
                answer[0] = start
                answer[1] = end
        end += 1
        if end >= len(sequence):
            break
        total += sequence[end]

    return answer