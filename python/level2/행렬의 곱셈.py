def solution(arr1, arr2):
    answer = []
    for i in range(0, len(arr1)):
        row = []
        for j in range(0, len(arr2[0])):
            element = 0
            for k in range(0, len(arr1[0])):
                element += arr1[i][k]*arr2[k][j]
            row.append(element)
        answer.append(row)
    return answer


# debug
arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))
