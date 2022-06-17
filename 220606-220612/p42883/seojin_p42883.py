from itertools import combinations


def solution(number, k):
    tmp = []
    for i in number:
        tmp.append(i)
    combi = list(combinations(tmp, len(number) - k))

    setting = []
    for com in combi:
        for i, j in enumerate(com):
            if i == 0:
                number = j
            else:
                number += j
        setting.append(number)
    setting = sorted(setting)
    return setting[-1]

## 시간초과뜨는데 다른 방법을 못찾겠음.