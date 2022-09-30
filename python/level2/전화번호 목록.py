def solution(phone_book):
    phone_book.sort()
    h = {}
    for i in range(len(phone_book)):
        for j in range(len(phone_book[i])):
            if h.get(phone_book[i][:j]):
                return False
        h[phone_book[i]] = True
    return True


# debug
phone_book = list(input().split())
print(solution(phone_book))
