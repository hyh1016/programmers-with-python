def solution(n, words):
    answer = [0, 0]
    used = set()
    start = words[0][0]
    for i in range(len(words)):
        if words[i] in used or words[i][0] != start:
            answer = [i%n+1, i//n+1]
            break
        used.add(words[i])
        start = words[i][-1]
    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])) # [3, 3]
