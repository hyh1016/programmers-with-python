def solution(s):
    mod_count, zero_count = 0, 0
    while s != '1':
        prev = len(s)
        result = s.count('1')
        zero_count += prev - result
        s = bin(result)[2:]
        mod_count += 1
    return [mod_count, zero_count]


print(solution('110010101001')) # [3, 8]
