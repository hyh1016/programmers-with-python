def solution(s):
    words = s.split(' ')
    new_words = []
    for word in words:
        if len(word) == 0:
            new_words.append('')
            continue
        new_word = word[0].upper()
        for i in range(1, len(word)):
            new_word += word[i].lower()
        new_words.append(new_word)
    return ' '.join(new_words)

# debug
# example: 3people unFollowed me
print(solution(input()))
