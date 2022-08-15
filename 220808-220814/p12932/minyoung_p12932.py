def solution(n):
    lst = list(map(int, list(str(n))))
    result = []

    for l in reversed(range(len(lst))):
        result.append(lst[l])
        
    return result